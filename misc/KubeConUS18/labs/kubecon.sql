drop database IF EXISTS kubecon;
create database kubecon;
use kubecon;
CREATE TABLE main (
      k varchar(255),
      v TEXT default NULL,
      PRIMARY KEY (k)
);
