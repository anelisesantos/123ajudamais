#!/bin/bash

bind_address="0.0.0.0:8000"
workers=4

# Executar o Gunicorn com as configurações personalizadas
gunicorn -b "$bind_address" -w "$workers" app:app
