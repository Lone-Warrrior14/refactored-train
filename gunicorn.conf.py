import os

# Gunicorn configuration file for Railway and high-load production environments

# Port binding
port = os.environ.get("PORT", "5000")
bind = f"0.0.0.0:{port}"

# Execution timeout in seconds (configurable via GUNICORN_TIMEOUT env variable, default 600s / 10 minutes)
# Set high to easily handle 50MB+ TIM master files and multiple MB52 Excel files without worker kills
timeout = int(os.environ.get("GUNICORN_TIMEOUT", "600"))

# Graceful timeout for worker shutdown
graceful_timeout = int(os.environ.get("GUNICORN_GRACEFUL_TIMEOUT", "60"))

# Keepalive for persistent connections
keepalive = int(os.environ.get("GUNICORN_KEEPALIVE", "15"))

# Worker concurrency
# In environments with memory constraints and heavy Pandas calculations, 2 workers with 4 threads is optimal
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
threads = int(os.environ.get("GUNICORN_THREADS", "4"))
worker_class = "gthread"

# Memory leak protection - restart worker after processing N requests
max_requests = int(os.environ.get("GUNICORN_MAX_REQUESTS", "500"))
max_requests_jitter = 50

# Logging
accesslog = "-"
errorlog = "-"
loglevel = os.environ.get("LOG_LEVEL", "info")
