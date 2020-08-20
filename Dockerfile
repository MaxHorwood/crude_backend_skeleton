FROM python:3.8.4-buster

COPY . /src
WORKDIR /src

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["python"]
CMD ["run.py"]