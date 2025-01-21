@echo off 
cd /d "%HOMEDRIVE%%HOMEPATH%\Documents\Scripts\walk_reminder"
call .venv\Scripts\activate
python main.py
exit