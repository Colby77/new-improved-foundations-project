FROM python:3.10.9-alpine3.17

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./backend /app

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]