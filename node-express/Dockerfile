FROM node:latest
MAINTAINER Ryan Kois "ryan.kois@gmail.com"

COPY . /app
WORKDIR /app

RUN npm install
ENTRYPOINT ["node"]
CMD ["index.js"]
