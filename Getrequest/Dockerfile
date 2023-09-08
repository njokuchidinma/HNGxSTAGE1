FROM python:3.10-slim

ENV PYTHONBUFFERED=1

ADD ./requirements.txt/app/requirements.txt

ADD ./app 
WORKDIR /app

RUN apt update -y

RUN pip install -r /app/requirements.txt

# collect statc files
RUN python manage.py makemigrations && python manage.py  migrate
RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--timeout", "600", "--workers", "1", "Getrequest.wsgi.application"]