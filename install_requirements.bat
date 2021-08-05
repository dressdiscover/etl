@ECHO OFF
cd %~dp0
CALL venv\Scripts\activate.bat
pip install ..\paradicms\etl
pip install -r ..\pastpy\requirements.txt
