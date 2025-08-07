# Use uma imagem base oficial do Python que seja compatível com seu projeto
FROM python:3.11-slim

# Instalação de dependências do sistema para WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libharfbuzz0b \
    libcairo2 \
    libgdk-pixbuf-2.0-0 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# O resto do arquivo permanece exatamente igual...
WORKDIR /app

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-dev --no-root
COPY . .
CMD ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]