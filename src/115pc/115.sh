#!/bin/sh
export LD_LIBRARY_PATH=/opt/115pc/lib:$LD_LIBRARY_PATH
export PATH=/opt/115pc:$PATH
# workaround under Wayland
export QT_QPA_PLATFORM=xcb
/bin/bash -c "exec -a $0 /opt/115pc/115 > /dev/null 2>&1" $0
