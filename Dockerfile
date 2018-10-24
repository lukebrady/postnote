# Container cloud will be run on the latest version of apache.
FROM php:7.2-apache

# Copy the code to the container.
# Will change to ./public-html/
RUN docker-php-ext-install pdo pdo_mysql
COPY ./src/ /var/www/html/
EXPOSE 80 443