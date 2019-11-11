#!/usr/bin/env python

import MySQLdb as mysql
import os
import sys
import time
from datetime import datetime

dping_host = os.getenv('DPING_HOST', 'localhost')
dping_port = os.getenv('DPING_PORT', 3306)
dping_user = os.getenv('DPING_USER', 'root')
dping_passwd = os.getenv('DPING_PASSWD', 'my-secret-pw')
dping_db = os.getenv('DPING_DB', 'dping')

try:
    db = mysql.connect(host=dping_host,user=dping_user,
                        passwd=dping_passwd,port=dping_port)

except mysql.MySQLError as err:
    print("Error: {}".format(err))
    sys.exit(1)

try:
    db.query('create database ' + dping_db)

except mysql.MySQLError as err:
    print("Warning: {}".format(err))

try:
    db.select_db(dping_db)

except mysql.MySQLError as err:
    print("Warning: {}".format(err))

try:
    db.query("""CREATE TABLE main (
                id int unsigned NOT NULL auto_increment,
                unixtime double default NULL,
                PRIMARY KEY (id)
              )""")
    db.close()

except mysql.MySQLError as err:
    print("Warning: {}".format(err))

try:
    db = mysql.connect(host=dping_host,user=dping_user,
                        passwd=dping_passwd,port=dping_port)
    db.select_db(dping_db)
    db.close()

except mysql.MySQLError as err:
    print("Error: {}".format(err))
    sys.exit(1)

while True:
    try:
        selected = "no result"
        hostname = "pending"
        connection = "0"

        db = mysql.connect(host=dping_host,user=dping_user,
                            passwd=dping_passwd,port=dping_port)
        db.select_db(dping_db)
        db.query("""SELECT connection_id() AS connection, @@hostname AS hostname,unixtime FROM `main` WHERE id=(SELECT MAX(id) FROM `main`)""");

        res = db.store_result()
        rows = res.fetch_row(maxrows=0,how=2)
        now = time.time()

        db.query("""INSERT INTO `main` SET unixtime=""" + str(now))
        db.commit()
        db.close()

        if len(rows) > 0:
            selected = rows[0]['main.unixtime']
            hostname = rows[0]['hostname']
            connection = rows[0]['connection']

        print "selected@" + hostname + ": " + str(selected) + \
              " (" + str(connection) + ")\n\ninserted@" + hostname + \
              ": " + str(now) + " (" + str(connection) + ")"

        sys.stdout.flush()

    except mysql.MySQLError as err:
        time.sleep(1)
