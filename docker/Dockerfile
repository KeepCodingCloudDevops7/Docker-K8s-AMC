FROM python:3.7-alpine as base

WORKDIR /install

RUN apk add --no-cache gcc musl-dev linux-headers curl mysql-client mysql-dev

WORKDIR /app
COPY requirements.txt ./

RUN pip install --prefix=/install -r requirements.txt

FROM base
RUN apk add --no-cache mysql-dev

COPY --from=base /install /usr/local

WORKDIR /app
COPY app.py ./

ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=user
ENV MYSQL_HOST=db
ENV MYSQL_DATABASE=db-partidos

EXPOSE 5000

CMD ["flask", "run"]