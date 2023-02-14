FROM python:3.10.9-alpine3.17

WORKDIR /app

COPY requirements.txt /app

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]