FROM python:3.9.5

RUN apt-get update

RUN apt-get -y install python

RUN pip install --upgrade pip

COPY . /questionare-portal 

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /questionare-portal 



RUN pip install -r /tmp/requirements.txt

# RUN pip freeze > requirements.txt

 

EXPOSE 8000

RUN ls
CMD ["python3","manage.py","runserver"]
