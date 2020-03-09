Welcome to the meteoscrapper project
==============================================

This is a simple web scrapper written in Python 3.8 and using Beautiful Soup 4 to scrap the observations of meteo.pf, transform them as à panda datafrrame and save it as json object in S3

What's Here
-----------

* README.md - this file
* meteoscrappey.py - this is the main program
* .gitignore

Deploy with cloud9
---------------
1. : Create a cloud9 environment 
1. Create an S3 bucket
2. Clone this project in you development environment
``` git clone https://github.com/HLeviel/meteoscrapper.git```
3. Run in local
  * Add dependencies
    ```venv/bin/pip install bs4 numpy pandas s3fs requests```
4. Deploy the function in Lambda 
6. Add permisson to Lambda to access the S3 bucket
7. Configure the trigger to start the function