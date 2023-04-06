FROM python:3.7-alpine as base

FROM base AS dependencies

WORKDIR /install

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt



FROM base

COPY --from=dependencies /install /usr/local

WORKDIR /app
COPY . .

ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=user
ENV MYSQL_HOST=kp_db
ENV MYSQL_DATABASE=db_partidos

EXPOSE 5000

CMD ["flask", "run"]