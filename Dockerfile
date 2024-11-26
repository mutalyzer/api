FROM python:3.13-slim

WORKDIR /usr/src/app

# required for building wheel packages
RUN apt-get update && apt-get install -y gcc g++ git

RUN pip install setuptools

# we can't just copy over setup.py and setup.cfg since it references the mutalyzer_api
COPY . .

RUN pip install .

EXPOSE 5000

CMD mutalyzer_api
