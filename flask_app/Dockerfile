FROM ubuntu:20.10
# MAINTAINER vyas.amit23vyas@gmail.com

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install gunicorn3 -y

COPY requirements.txt requirements.txt
COPY flaskapp /opt/

RUN pip3 install -r requirements.txt
WORKDIR /opt 

CMD ["gunicorn 3" , "-b", "0.0.0.0:8000", "app:app" , "--worker=5"] 