FROM python:3.9

WORKDIR /usr/src/milletContainer


COPY . .
RUN pip3 install --no-cache-dir -r backend/requirements.txt
RUN echo "python backend/manage.py makemigrations && python backend/manage.py migrate && python backend/manage.py runserver 0.0.0.0:8000" >> ./run.sh

EXPOSE 8000

CMD ["bash","run.sh"]

