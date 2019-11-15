#!/bin/sh

while [[ true ]]; do
	curl -s -XPOST --connect-timeout 300 ${POPULOUS_URL}
	sleep 1
done
