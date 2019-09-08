#!/bin/bash
set -e

NODES=0
TIMER=30
WAITING=${TIMER}
PROCS="dbus-daemon corosync pacemakerd cib stonithd lrmd attrd pengine crmd"

dbus-uuidgen --ensure
dbus-daemon --system --fork

set +e

echo -n "waiting for pod service names"
until host nfs-0.ha >/dev/null 2>&1 && host nfs-1.ha >/dev/null 2>&1 && host nfs-2.ha >/dev/null 2>&1; do
    echo -n .
    sleep 1
done

while ! service corosync start 2>&1 | grep '...done.'; do
    if [[ ${WAITING} -eq 0 ]]; then
        exit 1
    fi
    WAITING=$(expr ${WAITING} - 1)
    echo "waiting for corosync start (${WAITING}s)"
    sleep 1
done

WAITING=${TIMER}

while [[ ${NODES} -ne 3 ]]; do
    if [[ ${WAITING} -eq 0 ]]; then
        exit 1
    fi
    NODES=$(corosync-cmapctl | grep join_count | wc -l)
    WAITING=$(expr ${WAITING} - 1)
    echo "waiting for nodes to join (${WAITING}s, ${NODES} so far)"
    sleep 1
done

set -e

service pacemaker start

while [[ 1 ]]; do
    for PROC in ${PROCS}; do
        pidof ${PROC} >/dev/null
    done
	sleep 5
done
