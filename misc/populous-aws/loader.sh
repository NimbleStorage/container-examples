#!/bin/bash

for i in {1..16}; do 
	curl -XPOST --connect-timeout 300 http://${1}/api/populous &
done
wait
