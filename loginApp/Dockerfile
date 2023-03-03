FROM python:3.9-alpine
COPY . /loginapp
WORKDIR /loginapp
RUN chmod +x docker-entry-point.sh
RUN pip3 install -r requirements.txt
EXPOSE 5050
CMD ["python", "manage.py", "runserver", "0.0.0.0:5050"]