FROM python:3.9.17
MAINTAINER Eunbin Kwon <eun61n@gmail.com>

WORKDIR /app
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

WORKDIR /app/app
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
