FROM contraslash/alpine-django-deploy-common-s3

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD . /code/

# I really don't need to make the migrations in this docker file
# RUN python manage.py makemigrations

EXPOSE 8000

#CMD ["ash"]
CMD ["uwsgi", "--ini", "uwsgi.ini"]
