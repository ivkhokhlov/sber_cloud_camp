FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install poetry && \
    poetry config virtualenvs.create false &&  \
    poetry install --no-interaction --no-ansi --no-root
ENTRYPOINT ["poetry", "run", "python", "-m", "pytest"]
