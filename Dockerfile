FROM ubuntu 
RUN apt-get update && apt-get install -y apache2-utils
RUN apt-get install -y apache2 
RUN apt clean 
EXPOSE 80
CMD [“apache2ctl”, “-D”, “FOREGROUND”]


FROM mysql:latest
