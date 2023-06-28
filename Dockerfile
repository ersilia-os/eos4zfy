FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install requests==2.31.0
RUN pip install beautifulsoup4==4.12.2
RUN pip install pandas==1.3.5

WORKDIR /repo
COPY . /repo
