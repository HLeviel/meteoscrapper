Welcome to the meteoscrapper project
==============================================

This is a simple web scrapper written in Python 3.8 and using Beautiful Soup 4 to scrap the observations of meteo.pf, transform them as à panda datafrrame and save it as json object in S3

What's Here
-----------

* README.md - this file
* meteoscrappey.py - this is the main program
* .gitignore

Getting Started
---------------
0. Prerequisites : Install aws command line
1. Create an S3 bucket
2. Clone this project in you development environment
3. If you want to run it
  * Add permissions to write to S3 buckey
  * Add dependencies
    sudo python3 -m pip install bs4 numpy pandas s3fs
4. Deploy the function in Lambda 
  * Add permissions to deploy
5. Deploy the layer in Lambda
6. Add permisson to Lambda to access the S3 bucket
7. Configure the trigger to start the function