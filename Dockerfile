FROM python:3.7  AS build-env
RUN python3 ./init.py
CMD["./hello_world"]