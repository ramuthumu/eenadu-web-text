#!/bin/bash
if [ -e /opt/my_flask_app/server.pid ]; then
  kill -9 $(cat /opt/my_flask_app/server.pid)
  rm -f /opt/my_flask_app/server.pid
fi
