import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count()
user = "dzen"
max_requests = 500
timeout = 120
threads = 3
proc_name = "gunicorn"
env = 'LANG="en_US.utf8"'
