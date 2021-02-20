# FROM nginx:1.19.7-alpine
FROM richarvey/nginx-php-fpm:1.9.1

COPY nginx/nginx.conf /etc/nginx/nginx.conf

COPY nginx/sites-available/default.conf /etc/nginx/sites-available/default.conf

# COPY www /var/www/html

EXPOSE 80