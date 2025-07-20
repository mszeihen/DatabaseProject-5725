Docker mysql instructions

docker pull mysql:latest

docker run -d --name COP-5725-mysql -e MYSQL_ROOT_PASSWORD=COP5725 -p 3307:3306 mysql

docker exec -it COP-5725-mysql bash

$ mysql -u root -p

Enter password: COP5725

