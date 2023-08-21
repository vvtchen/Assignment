FROM python:3.10.6-alpine3.16
WORKDIR /backend
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY . .