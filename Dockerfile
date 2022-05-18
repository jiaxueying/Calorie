FROM python:3.9

WORKDIR /usr/src/milletContainer


COPY ./backend .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN echo "python manage.py makemigrations && python manage.py migrate && python manage.py runserver --skip-checks" >> ./run.sh

EXPOSE 8000

CMD ["bash","run.sh"]

