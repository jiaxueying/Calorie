FROM python:3.9

WORKDIR /usr/src/milletContainer

EXPOSE 8000 3306

COPY backend/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN echo "python backend/manage.py makemigrations && python backend/manage.py migrate && python backend/manage.py runserver" >> ./run.sh

COPY . .

CMD ["bash","run.sh"]

