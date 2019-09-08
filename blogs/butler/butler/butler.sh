#!/bin/bash
set -euxo pipefail

# This is a crude POC. Do not use for anything you care about
GANESHA_PID=/var/run/ganesha.pid
GANESHA_RETRY=5
GANESHA_RETRY_INTERVAL=5
GANESHA_EXPORT=/export
GANESHA_DEAD=0
MULTIWRITER_DEVICE=/dev/xvda

case $1 in
    start)
        mkfs.xfs ${MULTIWRITER_DEVICE} || true
        mount ${MULTIWRITER_DEVICE} ${GANESHA_EXPORT}
        echo "/dev/xvda /export xfs rw,relatime,attr2,inode64,noquota 0 0" >/etc/mtab
        service rpcbind start
        service nfs-common start
        ganesha.nfsd -L /var/log/ganesha/ganesha.log
        echo started
    ;;
    stop)
        set +e
        while [[ ${GANESHA_RETRY} -ne 0 ]] || [[ ${GANESHA_DEAD} -eq 0 ]]; do
            if [[ -e ${GANESHA_PID} ]]; then
                if ! kill $(cat ${GANESHA_PID}); then
                    if ! pidof ganesha.nfsd; then
                        echo ganesha is dead, ensure pid file is gone 
                        rm ${GANESHA_PID}
                    fi
                fi
                GANESHA_RETRY=$(expr ${GANESHA_RETRY} - 1)
                sleep ${GANESHA_RETRY_INTERVAL}
                echo retrying ${GANESHA_RETRY}
            else
                GANESHA_DEAD=1
                GANESHA_RETRY=0
                if mountpoint ${GANESHA_EXPORT}; then
                    umount ${GANESHA_EXPORT}
                fi
                service nfs-common stop
                service rpcbind stop
                echo -n "" >/etc/mtab
            fi
        done
        echo stopped
    ;;
    status)
        if pidof ganesha.nfsd; then
            echo running
        else
            exit 3
        fi
    ;;
    *)
        echo please invoke `basename $0` with start, stop or status as the only argument
    ;;
esac
