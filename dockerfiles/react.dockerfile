FROM node:18-alpine3.17

WORKDIR /app

COPY /frontend/package*.json /app

RUN npm i --silent

RUN npm i -g react-scripts@5.0.1

COPY /frontend /app

CMD [ "npm", "start", "--port", "3000" ]