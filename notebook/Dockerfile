FROM python:3.7.10

RUN apt-get update && apt-get -y install gcc libpq-dev
ENV PYTHONUNBUFFERED 1
COPY requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN mkdir /opt/notebook
COPY . /opt/notebook
WORKDIR /opt/notebook

EXPOSE 8000
