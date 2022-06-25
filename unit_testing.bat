@echo off
title ETL Unit Testing
call myvenv\Scripts\activate
call cd Scripts
python unit_testing.py
pause