# Use an official Python runtime as a parent image (debian based)
FROM python:3.10-slim

# Define environment variable
ENV FLASK_APP=routes.py

# Install any required packages
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# clone the basic app repo
RUN git clone https://github.com/jcfitzpatrick12/trusted-access-basic.git

# set the working directory as the cloned repo
WORKDIR /home/trusted-access-basic

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the the world outside this container
EXPOSE 5000

