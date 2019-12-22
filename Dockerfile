FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install matplotlib
RUN pip install pandas
RUN pip install sklearn
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt