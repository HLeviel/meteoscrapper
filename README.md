Welcome to the meteoscrapper project
==============================================

This is a simple web scrapper written in Python 3.8 and using Beautiful Soup 4 to scrap the observations of meteo.pf, transform them as à panda datafrrame and save it as json object in S3

What's Here
-----------

* README.md - this file
* meteoscrapper.py - this is the main program
* .gitignore
* requirements.txt - the dependencies

Deploy with cloud9
---------------
1. Create an S3 bucket
2. In a cloud9 environment, create a new lambda application (for example Application = meteo and Lamda = scrapper)
3. Get the code 
  * Right click on the application folder and Open a terminal window
  * Add dependencies
  
```python3 -m pip install bs4 numpy pandas s3fs requests -t .```
  * Replace the file scrapper/lambda_function.py with the function from github
  
```wget -O scrapper/lambda_function.py "https://github.com/HLeviel/meteoscrapper/raw/master/meteoscrapper.py"```
  * In the file scrapper/lambda_function.py update the S3 bucket name (don't forget trailing /)
  
```target_s3_bucket = "s3://my_bucket_name/"```

4. Test the function in local, should get "OK" result and a file in your bucket
5. Deploy the function in Lambda 
6. Add permisson to Lambda to access the S3 bucket
   * Navigate to the lambda functions applications list, 
   * Open the application 
   * Develop the function and open the role in a new window
   * Attach a policy 
   * Create a new policy and attach it to the role
     - Select S3
     - Allow PutObject and ListBucket 
     - Restrict to all objects of the target S3 bucket 
7. Configure the trigger to start the function
   * In the AWS console, navigate to the new lamda function 
   * Click on Trigger
   * Select the CloudWatch Event
   * Specify the rate : rate(1 hour) and activate the trigger
