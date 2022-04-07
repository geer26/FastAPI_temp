# Pull base image
FROM python:3.9

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install fastapi[all] fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn

COPY . /code/

EXPOSE 8000