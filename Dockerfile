# BUILD: docker build -t osc-party-app .

# --rm Automatically remove the container when it exits

# EDIT mode (shared src folder) 
# docker run -it --rm -p 8090:80 -p 4330:4330 -v $PWD/src:/var/www/html osc-party-app /bin/bash

# RUN
# SERVER mode: docker run -it --rm -p 8090:80 -p 4330:4330 osc-party-app # bind puerto 80 en docker a 8090 en localhost
# DEV mode (shared src folder): docker run -it --rm -p 8090:80 -p 4330:4330 -v $PWD/src:/var/www/html  --entrypoint /bin/bash osc-party-app

FROM php:7.0-apache

# NOTE: We provide the helper scripts docker-php-ext-configure, docker-php-ext-install, and docker-php-ext-enable to more easily install PHP extensions.
# https://hub.docker.com/_/php/

RUN apt-get update && apt-get install -y \
#  git \
  python \
  python-pip \
  python-dev \
  build-essential \
  screen \
  liblo-dev

# RUN git clone https://github.com/sonidosmutantes/osc-party
# RUN cp -R osc-party/src/ /var/www/html/
COPY src/ /var/www/html/
#COPY rc.local /etc/rc.local
#COPY config/php.ini /usr/local/etc/php/

WORKDIR /var/www/html/

RUN pip2 install --upgrade pip
RUN pip2 install cython
RUN pip2 install pyliblo
RUN pip2 install simplejson
RUN pip2 install -U https://github.com/google/google-visualization-python/zipball/master

# Downloads url (no need to install wget)
ADD http://code.jquery.com/jquery-1.8.2.min.js /var/www/html/

# js file to use with ni_graph.php (graph without internet connection)
ADD https://www.google.com/uds/api/visualization/1.0/84dc8f392c72d48b78b72f8a2e79c1a1/format+ru,default+ru,ui+ru,table+ru,corechart+ru.I.js /var/www/html/visualization.js

RUN chmod 755 /var/www/html/jquery-1.8.2.min.js
RUN chmod 755 /var/www/html/visualization.js

#useless google visualization api still needs an internet connection
#ADD https://www.google.com/jsapi /var/www/html
#RUN chmod 755 /var/www/html/jsapi

EXPOSE 4330
EXPOSE 80
#ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND && screen -S oscmon -d -m /var/www/html/pyOSCmon.py
ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND
