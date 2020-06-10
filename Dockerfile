#This is a typical example that should be running locally!

FROM python:3.7

COPY TeamInternationalBackend /TeamInternationalBackend
WORKDIR /TeamInternationalBackend
ADD requirements.txt /TeamInternationalBackend/

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
