FROM python:3.9-alpine

WORKDIR /CodeRunner

COPY ./app/ /CodeRunner/app
COPY ./requirements.txt /CodeRunner

RUN apk add  py3-pip openjdk8 \
	&& pip3 install -r requirements.txt

ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PATH="$JAVA_HOME/bin:${PATH}"

EXPOSE 8111

CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8111"]