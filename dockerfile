# Pull base image
#FROM python:3.9
FROM python:3.9-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
# Intstall ALP image dependencies - remove if image is ubuntu/debian based!
RUN apk update && apk add --no-cache g++ make libffi-dev musl-dev

# Install dependencies
RUN pip install fastapi[all] fastapi-sqlalchemy pydantic alembic psycopg2-binary uvicorn

COPY ./backend/ /code/

EXPOSE 8000