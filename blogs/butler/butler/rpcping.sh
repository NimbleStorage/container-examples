#!/bin/bash
HOST=${1:-nfs}

while [[ 1 ]]; do
    NOW=$(date +%s.%N)
    while ! rpcinfo -l ${HOST} nfs 4 2>/dev/null | grep nfs >/dev/null; do
        sleep 0.1
    done
    LATER=$(date +%s.%N)
    echo -n "$(date) rpcinfo responded: "
    echo "scale = 2; ${LATER} - ${NOW}" | bc
    sleep 0.3
done
