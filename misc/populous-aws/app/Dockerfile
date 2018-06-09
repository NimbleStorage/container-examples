FROM alpine:latest
MAINTAINER michael.mattsson@hpe.com

WORKDIR /tmp
ADD requirements.txt /tmp

RUN apk update \
	&& apk add py-pip py-pillow py-gunicorn py-requests \
	&& pip install -r requirements.txt

ADD https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-8.0.11.tar.gz /tmp/

RUN tar xzvf mysql-connector-python-8.0.11.tar.gz \
	&& cd mysql-connector-python-8.0.11 \
	&& python setup.py install \
	&& cd .. \
	&& rm -rf /tmp/*

RUN mkdir -p /app/run
WORKDIR /app
ADD *.py /app/run/
ADD template.json /app/run/

EXPOSE 8000

WORKDIR /app/run
ARG BUILD_TAG
RUN echo -n $BUILD_TAG > VERSION

CMD [ "gunicorn", "-b", "0.0.0.0", "-t", "300", "--threads", "4", "populous:api" ]
