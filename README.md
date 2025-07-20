Docker mysql instructions
docker pull mysql:latest
docker run --name COP-5725-mysql -e MYSQL_ROOT_PASSWORD=COP5725 -d mysql
docker exec -it COP-5725-mysql bash


