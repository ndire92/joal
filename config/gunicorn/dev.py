"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "Stud.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "0.0.0.0:8001"
# Restart workers when code changes (development only!)
reload = True
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/jdev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/www/vhosts/precvadi-commune.sn/joalfadiouth.precvadi-commune.sn/config/gunicorn/joal.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True

