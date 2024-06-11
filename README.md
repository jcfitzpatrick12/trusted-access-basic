# Basic Flask App

Basic containerised flask application for testing.

# Run instructions
The following instructions can be used to run the trusted-access-basic flask web server locally.
- Clone the github repo:  
```git clone https://github.com/jcfitzpatrick12/trusted-access-basic.git```
- Build the image:  
```docker build --no-cache -t flask-test-image .```  
- Make the run script executable:  
```chmod +x ./run.sh```  
- Run the flask web server:  
```./run.sh```
- Visit the following web-page in your preferred browser:
```http://0.0.0.0:5000/```  
