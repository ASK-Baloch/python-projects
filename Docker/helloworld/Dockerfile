FROM ubuntu:22.04
FROM python:3.12
RUN pip install poetry
WORKDIR /code
ADD ./pyproject.toml ../helloworld /code/ 
RUN poetry install
CMD [ "poetry","run","uvicorn","helloworld.main.py:app","--host","0.0.0.0" ]  