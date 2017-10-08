FROM python:3.6

LABEL maintainer="d.renault@karudev-informatique.fr"

# Install Ubuntu packages
RUN apt-get update
RUN apt-get install alien dpkg-dev debhelper build-essential libaio1 vim-nox --assume-yes

# Install python app
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

USER root


