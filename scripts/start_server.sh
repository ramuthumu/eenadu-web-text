#!/bin/bash
mkdir -p /opt/my_flask_app
cd /opt/my_flask_app
source venv/bin/activate
export FLASK_APP=app.py # Replace 'application.py' with the name of your Flask app's entry point if it's different.
nohup flask run --host=0.0.0.0 --port=80 > server.log 2>&1 &
echo $! > server.pid
