import os

workers = int(os.environ.get('GUNICORN_PROCCESS','2'))

threads = int(os.environ.get("GUNİCON_THREADS",'4'))

#timeout

# timeout = int(os.environ.get('GUNICORN_TIMEOUT', '120'))

bind = os.environ.get('GUNICORN_BIND','0.0.0.0:8080') # PORT Maybe need to change


forwarded_allow_ips = '*'

secure_scheme_headers = {'X-Forwarded-Proto' : 'https' }
