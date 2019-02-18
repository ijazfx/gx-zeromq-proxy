FROM alpine:3.8

RUN apk add python py-zmq

COPY msgqueue.py .
COPY pubsub.py .
COPY main.py .

ENV ROUTER_PORT=60051
ENV DEALER_PORT=60052
ENV PUB_PORT=60053
ENV SUB_PORT=60054

EXPOSE $ROUTER_PORT
EXPOSE $DEALER_PORT
EXPOSE $PUB_PORT
EXPOSE $SUB_PORT

ENTRYPOINT ["python", "main.py"]