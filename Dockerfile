# Development Dockerfile to make testing easier under a standardized environment.
# XXX Do not use for production as-is

FROM python:2.7
LABEL maintainer Ginkgo Bioworks <devs@ginkgobioworks.com>

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --assume-yes apt-utils
RUN apt-get install --assume-yes \
    swig \
    libopenbabel-dev

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

RUN pip install pip-tools==1.9.0rc2
COPY requirements.txt ./
RUN pip install --requirement requirements.txt

COPY . ./
RUN pip install --editable .
EXPOSE $SERVER_PORT
CMD ["make", "test"]
