FROM python:3

WORKDIR /usr/src/milletContainer

COPY backend/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD "python3", "backend/manage.py","migrate" && "python3", "backend/manage.py","runserver" 
