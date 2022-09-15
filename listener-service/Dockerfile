FROM python:3
ENV PATH /usr/src/app/bin:$PATH
WORKDIR /app

RUN git clone https://github.com/edenhill/librdkafka.git
WORKDIR /app/librdkafka
RUN /app/librdkafka/configure --prefix /usr
RUN make
RUN make install

WORKDIR /app

RUN pip3 install confluent-kafka

CMD ["sleep", "99999"]