CREATE TABLE main (
	  id int unsigned NOT NULL auto_increment,
	  guid varchar(36) NOT NULL,
	  pid bigint default NULL,
	  street varchar(255) default NULL,
	  zip varchar(10) default NULL,
	  city TEXT default NULL,
	  email varchar(255) default NULL,
	  name varchar(255) default NULL,
	  imprint longblob,
	  PRIMARY KEY (id)
) AUTO_INCREMENT=10000000;
ALTER TABLE main ADD INDEX guid (guid);
