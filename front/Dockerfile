FROM node:16-alpine 
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "/app/src/index.js"]