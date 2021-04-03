# This project is based on https://github.com/ToxicCrack/PrintABrick
FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive


# for usage in Korea
#RUN sed -i -re 's/([a-z]{2}.)?archive.ubuntu.com|security.ubuntu.com/ftp.harukasan.org/g' /etc/apt/sources.list
#RUN sed -i -re 's/([a-z]{2}.)?archive.ubuntu.com|security.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list


# install required packages
RUN apt update
RUN apt -y install apt-utils tzdata vim wget software-properties-common unzip admesh build-essential libboost-all-dev 
RUN apt -y install libz-dev libpng-dev libjpeg-dev libtiff-dev python-numpy qt4-default libosmesa6-dev npm git gulp
RUN apt -y install autoconf
RUN npm install -g bower



# install php related packages
RUN add-apt-repository ppa:ondrej/php
RUN apt -y install php7.0 php7.0-fpm php7.0-dom php7.0-curl php7.0-ftp php7.0-soap php7.0-gd php7.0-pdo php7.0-zip php7.0-mbstring php7.0-intl php7.0-mysql

RUN sed -i -re 's/;date.timezone =/date.timezone = Asia\/Seoul/g' /etc/php/7.0/cli/php.ini

RUN echo "Asia/Seoul" > /etc/timezone
RUN rm -rf /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata


# get the source
#COPY ./project /PrintABrick
WORKDIR /tmp
RUN wget https://github.com/morcavon/PrintABrick/archive/refs/heads/master.zip -O master.zip
RUN unzip -d / master.zip
RUN mv /PrintABrick-master /PrintABrick


# prepare pov ray
WORKDIR /PrintABrick
RUN wget https://github.com/POV-Ray/povray/archive/refs/tags/v3.7.0.7.zip -O povray.zip
RUN unzip povray.zip
WORKDIR povray-3.7.0.7

RUN cd unix; ./prebuild.sh ; 
RUN ./configure COMPILED_BY="docker" --prefix=/usr
RUN make -j$((`nproc`-1)) && make install



# prepare stl2pov
WORKDIR /PrintABrick
RUN wget https://github.com/rsmith-nl/stltools/archive/refs/tags/3.3.zip -O stltools.zip
RUN unzip stltools.zip
RUN ln -sf /PrintABrick/stltools-3.3/stl2pov.py /usr/bin/stl2pov


# prepare ldview
RUN wget https://github.com/tcobbs/ldview/archive/refs/tags/v4.3.zip -O ldview.zip
RUN unzip ldview.zip
WORKDIR ldview-4.3
RUN make -j$((`nproc`-1)) -C OSMesa && make -C OSMesa install
RUN cp OSMesa/ldviewrc.sample ~/.ldviewrc


# install back-end
WORKDIR /PrintABrick
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/76a7060ccb93902cd7576b67264ad91c8a2700e2/web/installer -O - -q | php -- --quiet
RUN ./composer.phar update
RUN ./composer.phar install
RUN php bin/symfony_requirements


# install front-end
RUN npm install
RUN bower install --allow-root
RUN gulp default --env production

ENTRYPOINT /PrintABrick/entrypoint.py

