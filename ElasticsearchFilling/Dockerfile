FROM python:3-alpine
COPY . /
WORKDIR /
RUN pip3 install -r requirements.txt && \
    apk add --no-cache unzip && \
    apk add --no-cache wget && \
    apk add --no-cache openssh && \
    apk add --no-cache bash && \
    chmod +x wait-for
CMD python3 main.py