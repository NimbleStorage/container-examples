FROM mariadb:latest
ADD main.sql /docker-entrypoint-initdb.d
ADD mysqld.cnf /etc/mysql/mysql.conf.d

ARG BUILD_TAG=unknown
RUN echo -n $BUILD_TAG > VERSION
