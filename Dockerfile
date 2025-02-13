FROM ubuntu:latest
LABEL authors="dmitrijkalandarov"

ENTRYPOINT ["top", "-b"]