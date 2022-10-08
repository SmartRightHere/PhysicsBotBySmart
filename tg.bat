@echo off

call %~dp0telegrambot\telegram.py
cd telegrambot

set token=5498576111:AAEvfnKhVzQCbbxQH6ket8Qx-J-gduxZoTc

python telegram.py

pause
