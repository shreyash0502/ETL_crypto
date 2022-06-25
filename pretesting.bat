@echo off
title ETL Pretesting
echo ****Welcome to ETL Pretesting Environment****
pause
call myvenv\Scripts\activate
call cd Scripts
python pretests.py
pause