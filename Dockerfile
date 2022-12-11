FROM python:3.9-alpine
COPY . /BynderAPI
WORKDIR /BynderAPI
RUN pip install -r requirements.txt
RUN cd test
ENTRYPOINT pytest