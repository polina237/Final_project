from ubuntu:20.04
MAINTAINER Polina Golubeva
RUN apt-get update -y
COPY . /opt/Final_project
WORKDIR /opt/Final_project
RUN apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 app.py
