# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/playwright:focal
COPY . /app
WORKDIR /app
RUN mkdir vids && mkdir thumbs

RUN pip3 install -r requirements.txt
RUN python -m playwright install webkit
