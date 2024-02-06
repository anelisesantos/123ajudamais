bind = "0.0.0.0:8000"  # Especifique o endereço IP e a porta em que o Gunicorn deve ouvir
workers = 4  # Número de workers (processos) Gunicorn
worker_class = "sync"  # Tipo de worker (sync, gevent, etc.)
accesslog = "-"  # Arquivo de log de acesso (use "-" para stdout)
errorlog = "-"  # Arquivo de log de erros (use "-" para stdout)
