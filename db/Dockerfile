FROM mysql:5.7

COPY db/init.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=root

EXPOSE 3306

CMD ["mysqld"]
