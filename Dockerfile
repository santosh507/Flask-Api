FROM python:3.6.0
USER root
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi
WORKDIR /opt/app-root/src

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY ./server-conf/nginx.conf /etc/nginx/
COPY ./server-conf/flask-site-nginx.conf /etc/nginx/conf.d/
COPY ./server-conf/uwsgi.ini /etc/uwsgi/
COPY ./server-conf/supervisord.conf /etc/supervisor/conf.d/

COPY . ./
CMD ["/usr/bin/supervisord"]