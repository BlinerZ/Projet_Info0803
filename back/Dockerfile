FROM python:3.6

EXPOSE 5000

WORKDIR /back

ADD back/requirements.txt /back

RUN pip install -r requirements.txt

ADD back/app.py /back
CMD ["python", "app.py"]
