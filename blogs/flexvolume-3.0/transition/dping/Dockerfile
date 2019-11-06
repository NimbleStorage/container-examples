FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y \
    python-dev \
    default-libmysqlclient-dev \
    python-pip
RUN pip install mysqlclient
ADD dping.py /usr/local/bin/dping.py
ENTRYPOINT dping.py
