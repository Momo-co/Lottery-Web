# Base Image
FROM python:latest

# Working directory
WORKDIR /service_2

# Things we need in a container
COPY . .

# Install 
RUN pip3 install -r requirements.txt

# Ports to expose
EXPOSE 5000

# Entrypoint
ENTRYPOINT ["python3", "app.py"]