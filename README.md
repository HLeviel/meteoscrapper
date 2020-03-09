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
1. Create an S3 bucket
2. Create a cloud9 environment, and in the AWS Resources, create a new lambda application (for example application = meteo and Lamda = scrapper)
3. Get the code 
  * Navigate to your application folder
```cd meteo```
  * Add dependencies
```python3 -m pip install bs4 numpy pandas s3fs requests -t .```
  * Replace the file scrapper/lambda_function.py with the function from github
```wget -O scrapper/lambda_function.py "https://github.com/HLeviel/meteoscrapper/raw/master/meteoscrapper.py"```
4. Test the function in local 
5. Deploy the function in Lambda 
6. Add permisson to Lambda to access the S3 bucket
7. Configure the trigger to start the function