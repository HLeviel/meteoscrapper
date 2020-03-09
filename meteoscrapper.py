import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import datetime

target_s3_bucket = "s3://meteoscrapper/"

website_url = "https://meteo.pf/fr/observations-stations-iles"


def scrapper():
    # Read page
    response = requests.get(website_url)
    page = response.text

    # Parse page to extract observations
    parser = BeautifulSoup(page, 'html.parser')
    observations = parser.find("div", {"class":"station-group"}) 
    
    # Get title
    title = observations.find("h2").text
    
    # Build date
    splitted_title = title.split(" ")
    day = int(splitted_title[3])
    month_to_number = {"janvier":1, "février" : 2, "mars" : 3, "avril" : 4, "mai" : 5, "juin" : 6, "juillet" : 7, 
    "août" : 8,	"septembre" : 9, "octobre" : 10, "novembre" : 11, "décembre" : 12}
    month = month_to_number[splitted_title[4]]
    year = int(splitted_title[5])
    hour =  int(splitted_title[7])
    date = datetime.datetime(year, month, day, hour)
    
    # Get stations
    stations = observations.find_all("div", {"class":"station"})
    data=[]
    for station in stations:
        station_data = dict(station = station.find("h3", {"class":"decorate"}).text, date = date)
        
        # Iterate over measures
        for measure in station.find_all( "li"):
            station_data[measure.find("div", {"class":"station-title"}).text] = measure.find("div", {"class":"station-text-left"}).text
        data.append(station_data)
    
    # Clean data
    angle_to_number = {"NORD" : 0, "NORD-EST" : 45, "EST" : 90, "SUD-EST" : 135, "SUD" : 180, 
    "SUD-OUEST" : 225, "OUEST" : 270, "NORD-OUEST" : 315}
    sky_to_number = {"PAS OBSERVE" : -1, "CIEL DEGAGE" : 2, "PEU NUAGEUX" : 4, "NUAGEUX" : 6, "TRES NUAGEUX" : 8, "COUVERT" : 10}
    try:
        df = pd.DataFrame(data)
        df["Pression"] = df["Pression"].str.split(' ', 1).str.get(0).astype(int)
        df["Température"] = df["Température"].str.split(' ', 1).str.get(0).astype(int)
        df["Humidité"] = df["Humidité"].str.split(' ', 1).str.get(0).astype(int)
        df["Force du vent"] = np.where(df["Force du vent"]== '//', -1, df["Force du vent"].str.split(' ', 1).str.get(0).astype(int))
        df["Etat du ciel"] = df["Etat du ciel"].map(sky_to_number)
        df["Direction du vent"] = df["Direction du vent"].map(angle_to_number)
    except ValueError:
        print("Erreur de conversion" )
        print(page)
        return "Error"
        
    # Save data
    df.to_csv(''.join([target_s3_bucket, title, '.csv']), index=False)
    return "OK"

def lambda_handler(event, context):
    return scrapper()

if __name__ == "__main__":
    scrapper()
