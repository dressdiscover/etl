@ECHO OFF
cd %~dp0
poetry run python -m paradicms_gui.aws_site_creator -c config\aws_site\dressdiscover.org.cfg %*
