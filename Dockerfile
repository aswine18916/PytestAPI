FROM python:3.9-alpine
ADD . /BynderAPI
WORKDIR /BynderAPI
RUN pip install -r requirements.txt
RUN chmod +x test.sh
RUN ./test.sh