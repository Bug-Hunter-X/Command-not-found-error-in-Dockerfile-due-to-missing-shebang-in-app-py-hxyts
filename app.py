#!/usr/bin/env python3

print("Hello from app.py")

FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN chmod +x ./app.py
CMD ["/app/app.py"]