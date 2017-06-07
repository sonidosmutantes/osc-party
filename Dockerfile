<<<<<<< HEAD
# docker build -t osc-party-app .
# --rm Automatically remove the container when it exits
# docker run -it --rm -p 8090:80 -p 12345:12345 osc-party-app /bin/bash # bind puerto 80 en docker a 8080 en localhost

# EDIT mode (shared src folder) 
# docker run -it --rm -p 8090:80 -p 12345:12345 -v $PWD/src:/var/www/html osc-party-app /bin/bash
=======
# BUILD: docker build -t osc-party-app .

# RUN
# SERVER mode: docker run -it --rm -p 8090:80 -p 12345:12345 osc-party-app # bind puerto 80 en docker a 8090 en localhost
# DEV mode (shared src folder): docker run -it --rm -p 8090:80 -p 12345:12345 -v $PWD/src:/var/www/html  --entrypoint /bin/bash osc-party-app
>>>>>>> 98b440d343c4673abd4bff08cb2cef70ced75325

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

#COPY config/php.ini /usr/local/etc/php/

WORKDIR /var/www/html/

RUN pip2 install --upgrade pip
RUN pip2 install cython
RUN pip2 install pyliblo
RUN pip2 install simplejson
RUN pip2 install -U https://github.com/google/google-visualization-python/zipball/master

# Downloads url (no need to install wget)
ADD http://code.jquery.com/jquery-1.8.2.min.js /var/www/html/
ADD https://www.google.com/jsapi /var/www/html

RUN chmod 755 /var/www/html/jquery-1.8.2.min.js 
RUN chmod 755 /var/www/html/jsapi 

EXPOSE 4330
EXPOSE 80
ENTRYPOINT /usr/sbin/apache2ctl -D FOREGROUND && screen -d -m /var/www/html/pyOSCmon.py
