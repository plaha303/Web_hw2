# syntax=docker/dockerfile:1


ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV APP_HOME /app

WORKDIR $APP_HOME

# Copy the source code into the container.
COPY . .

RUN pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
ENTRYPOINT ["python", "__main__.py"]
