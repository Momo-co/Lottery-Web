# Base Image
FROM python:latest

# Dependency installation
RUN sudo apt install curl -y
RUN sudo apt update
RUN sudo apt install -y curl jq
RUN version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
RUN sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN sudo chmod +x /usr/local/bin/docker-compose

# Working directory
WORKDIR /service_1

# Things we need in a container
COPY . .

# Ports to expose
EXPOSE 5000

# Entrypoint
ENTRYPOINT ["python3", "app.py"]
