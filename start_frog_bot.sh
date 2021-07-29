#!/bin/bash

# @reboot ~/frog_bot/start_frog_bot.sh >> ~/frog_bot/logs.txt 2>&1

sleep 10
cd ~/frog_bot/
source ~/frog_bot/venv/bin/activate
python main.py

