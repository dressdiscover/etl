@ECHO OFF
cd %~dp0
CALL venv\Scripts\activate.bat
set PYTHONPATH=%PYTHONPATH%;..\..\paradicms\etl
set PYTHONPATH=%PYTHONPATH%;..\..\pastpy
python -m paradicms_etl.aws_site_creator -c config\aws_site\dressdiscover.org.cfg %*
