FROM python:3.8
COPY webapp.py /tmp/
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
CMD ["python", "/tmp/webapp.py"]
EXPOSE 80
