#!/bin/bash
set -e

apt-get update
apt-get install -y python3 python3-pip git

APP_DIR="/opt/app"
REPO_URL="https://github.com/Learnwithkarthik/vm-flask-login-app.git"

if [ ! -d "$APP_DIR" ]; then
  git clone $REPO_URL $APP_DIR
fi

cd $APP_DIR

pip3 install -r requirements.txt

nohup python3 app.py > /var/log/app.log 2>&1 &
