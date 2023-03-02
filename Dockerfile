# Dockerfile

# pull the official docker image
FROM python:3.10

# set work directory
WORKDIR /happy_milkman

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt /happy_milkman/
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /happy_milkman/