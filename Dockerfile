FROM python:3.6.9-alpine3.10

COPY echo-server.py /

EXPOSE 65432
ENTRYPOINT ["python3", "echo-server.py"]