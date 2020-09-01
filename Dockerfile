FROM python:3.7-alpine

COPY src/auth.py /src/
COPY bots/favretweet.py /src/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "main.py"]