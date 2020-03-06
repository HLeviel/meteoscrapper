Welcome to the meteoscrapper project
==============================================

This is a simple web scrapper written in Python 3.8 and using Beautiful Soup 4 to scrap the observations of meteo.pf, transform them as à panda datafrrame and save it as json object in S3

What's Here
-----------

This sample includes:

* README.md - this file
* meteoscrappey.py - this is the main program

Getting Started
---------------
0 - Prerequisites : Install aws command line
1 - Clone this project in you development environment
2 - Create an S3 bucket
3 - Add dependencies
sudo python3 -m pip install bs4 numpy pandas s3fs
4 - Deloy the function in Lambda 
5 - Deploy the layer in Lambda
6 - Add permisson to Lambda to access the S3 bucket
7 - Configure the trigger to start the function