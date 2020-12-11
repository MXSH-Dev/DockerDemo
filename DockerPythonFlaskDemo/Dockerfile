FROM python:alpine3.9

WORKDIR /home/app

COPY requirements.txt /home/app

RUN pip install -r requirements.txt

COPY ./src /home/app

CMD [ "python","app.py" ]