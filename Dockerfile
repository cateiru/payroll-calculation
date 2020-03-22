FROM python:3.6

COPY /src /src
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv --no-cache-dir
RUN pipenv install --system --deploy

CMD [ "python", "src/main.py" ]
