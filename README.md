# Basic Flask App

Basic containerised flask application for testing.

# Run instructions
- Clone the github repo:  
```git clone https://github.com/jcfitzpatrick12/trusted-access-basic.git```
- Build the image:  
```docker build --no-cache -t flask-test-image .```  
- Make the run script executable:  
```chmod +x ./run.sh```  
- Run the flask web server:  
```./run.sh```  