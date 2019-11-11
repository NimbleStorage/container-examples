FROM ubuntu:latest
RUN apt-get update && apt-get install -y python
ADD app3.py /
WORKDIR /
ENTRYPOINT /app3.py
