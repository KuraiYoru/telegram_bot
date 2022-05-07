@echo off

call %~dp0python_bot\venv\Scripts\activate

cd %~dp0python_bot

set TOKEN=5267269355:AAE1LFAtj2AlssUzUGSUMd-Ozf6X4bvFgGQ

python bot.py

pause