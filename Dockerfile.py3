# Development Dockerfile to make testing easier under a standardized environment.
# XXX Do not use for production as-is

FROM python:3.5
LABEL maintainer Ginkgo Bioworks <devs@ginkgobioworks.com>

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --assume-yes apt-utils
RUN apt-get install --assume-yes \
    libopenbabel-dev \
    openbabel \
    swig

ARG GIT_USER_NAME="Pychemy Default"
ARG GIT_USER_EMAIL="devs@ginkgobioworks.com"

RUN git config --global user.name "$GIT_USER_NAME" \
    && git config --global user.email "$GIT_USER_EMAIL"

ARG DEBIAN_FRONTEND=noninteractive
ENV PYCHEMY_HOME=/usr/src/pychemy
ENV SERVER_IP=0.0.0.0
ENV SERVER_PORT=8081

RUN mkdir -p $PYCHEMY_HOME
WORKDIR $PYCHEMY_HOME

RUN pip3 install pip-tools==1.9.0

COPY requirements.txt ./
RUN pip3 install --requirement requirements.txt

COPY . ./
RUN pip3 install --editable .

EXPOSE $SERVER_PORT
CMD ["make", "test"]

# vim: set ft=dockerfile :
