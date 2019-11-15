#!/usr/bin/env python

import os
import time
import datetime
from os import path

if not os.path.exists('data'):
    os.mkdir('data')

while True:
    log = "%s logging app3 from %s LoadAVG-1m: %s\n" \
        % (datetime.datetime.now(), os.uname()[1], round(os.getloadavg()[0],2))
    f = open("data/log.txt", "a")
    f.write(log)
    f.close()
    print log,
    time.sleep(1)
