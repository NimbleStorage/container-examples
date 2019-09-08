FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y \
      pacemaker \
      corosync \
      crmsh \
      xfsprogs \
      nfs-ganesha-xfs \
      host \
      bc && \
      rm -rf /var/lib/apt/lists/*
ADD entrypoint.sh /entrypoint.sh
ADD ganesha.conf /etc/ganesha/ganesha.conf
ADD butler.sh /etc/init.d/butler
ADD rpcping.sh /usr/local/bin/rpcping
ADD cib.xml /var/lib/pacemaker/cib/cib.xml
RUN mkdir /export && \
    mkdir /var/run/dbus && \
    mkdir -p /run/sendsigs.omit.d/rpcbind 
ENTRYPOINT /entrypoint.sh
