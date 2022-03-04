
# python 3.7 image 사용
FROM python:3.8-slim-buster

# 컨테이너의 작업 directory 설정
WORKDIR /app


RUN apt update -y && \
  apt install gcc -y   

COPY ./requirements.txt .
# dependencies Install
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run","--host=0.0.0.0"]


