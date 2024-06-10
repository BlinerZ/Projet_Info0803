FROM python:latest

EXPOSE 80

WORKDIR /front

ADD front/requirements.txt /front

RUN pip install -r requirements.txt

ADD front/app.py /front

CMD ["python", "app.py"]
