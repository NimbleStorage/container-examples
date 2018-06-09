import falcon
import json
import imprint
import requests
import mysql.connector
import sys

from os import environ
from time import time 

class PingResource:
    def __init__(self):
        self.v = version()

    def on_get(self, req, resp, **kwargs):

        db = Ping()

        ping = {
            'response_time_ms': db.response_time,
            'served_by': environ['HOSTNAME'],
            'version': self.v
        }
        
        resp.body = json.dumps(ping)

class ImprintResource:
    def on_get(self, req, resp):
        resp.set_header('Content-Type', 'image/png')
        resp.body = imprint.main()

class PopulousResource:
    def on_post(self, req, resp):
        f = open('template.json', 'r')
        r = requests.post('%s/api/process.php?request=data' % \
                (environ['DATAGEN']), data=json.dumps(json.load(f)))

        db = Populate()

        for row in r.json():
            db.insert(row['guid'], row['name'], row['zip'], row['city'], \
                    row['pid'], row['street'], row['email'], imprint.main())

        db.commit()

        resp.body = json.dumps({ 'status': 200 })

class DbConnect:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user=environ['POPULOUS_USER'], \
                        password=environ['POPULOUS_PASSWORD'], \
                        host=environ['POPULOUS_HOST'], \
                        db=environ['POPULOUS_DB'])

        except Exception:
            raise falcon.HTTPServiceUnavailable()

class Populate:
    def __init__(self):

        self.cnx = DbConnect().cnx
        self.cursor = self.cnx.cursor()

        self.stmt = ("INSERT INTO main " 
                     "(guid, name, zip, city, pid, street, email, imprint) " 
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                    
    def insert(self, guid, name, zip, city, pid, street, email, imprint):
        self.cursor.execute(self.stmt, (guid, name, zip, city, pid, street, email, imprint))
    
    def commit(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

class CensusResource:
    def on_get(self, req, resp):

        db = Census()

        census = {
            'census': db.census
        }

        resp.body = json.dumps(census)

class Census:
    def __init__(self):

        self.census = 0

        cnx = DbConnect().cnx
        cursor = cnx.cursor()

        query = "SHOW TABLE STATUS"
        cursor.execute(query)

        rows = cursor.fetchall()
        self.census = rows[0][4]
        
        cursor.close()
        cnx.close()

class Ping:
    def __init__(self):

        self.response_time = 0

	t1 = time()

        cnx = DbConnect().cnx
        cursor = cnx.cursor()

        query = ("SELECT * "
		 "  FROM main AS r1 JOIN "
       		 "    (SELECT CEIL(RAND() * "
                 "       (SELECT MAX(id) "
                 "         FROM main)) AS id) "
        	 "     AS r2 "
		 "WHERE r1.id >= r2.id "
		 "ORDER BY r1.id ASC "
		 "LIMIT 1")

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()
        cnx.close()
        
	t2 = time() 
	self.response_time = (t2 - t1) * 1000

def error_serializer(req, resp, exception):
    resp.body = exception.to_json()

def version():
    try:
        f = open('VERSION')
        version = f.read()
    except Exception:
        version = 'unknown'

    return version

 
api = falcon.API()
api.set_error_serializer(error_serializer)
api.add_route('/api/populous', PopulousResource())
api.add_route('/api/census', CensusResource())
api.add_route('/api/_ping', PingResource())
api.add_route('/api/_imprint', ImprintResource())
