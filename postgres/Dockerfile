FROM postgres:14

RUN apt-get update && apt-get install -y gettext-base

COPY postgresql.conf /etc/postgresql/postgresql.conf
COPY pg_hba.conf /etc/postgresql/pg_hba.conf
RUN mkdir -p "/var/log/postgresql/"

EXPOSE 5454

CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf", "-c", "hba_file=/etc/postgresql/pg_hba.conf"]
