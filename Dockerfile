FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./

COPY src/ ./src/
COPY README.md ./

ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.2.0

RUN pip install --no-cache-dir .

ENTRYPOINT ["dataproc"]
CMD ["--help"]
