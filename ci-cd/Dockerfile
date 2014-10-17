FROM fedora:20
MAINTAINER Neependra Khare
RUN yum install -y nginx vim supervisor gcc python-devel
RUN yum install -y python-pip
RUN pip install flask
RUN pip install uwsgi
ADD app_config/supervisord.conf /etc/supervisord.conf
ADD app_config/nginx-app.conf /etc/nginx/conf.d/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD app_config/uwsgi.ini /uwsgi.ini
ADD app_config/uwsgi_params /uwsgi_params
CMD ["/usr/bin/supervisord"]

