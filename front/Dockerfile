FROM node:16-alpine as build-stage

# 작업 디렉토리
WORKDIR /react-app

# json 파일 COPY
COPY package*.json ./

# npm install
RUN npm install

# react src folder copy
COPY src ./src

# react pulbic folder copy
COPY public ./public

# nginx config file copy
COPY addition_container_server.conf ./

# nginx build
RUN npm run build


FROM nginx:1.15
# nginx default.config remove
RUN rm /etc/nginx/conf.d/default.conf

# copy our config
COPY --from=build-stage /react-app/addition_container_server.conf /etc/nginx/conf.d/

# copying production build from last stage to serve through nginx
COPY --from=build-stage /react-app/build/ /usr/share/nginx/html

# exposing port 8080 on container
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]