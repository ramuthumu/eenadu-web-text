#!/bin/bash
cd /opt/my_flask_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
