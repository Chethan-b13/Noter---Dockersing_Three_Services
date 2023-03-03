FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip3 install -r Requirements.txt
EXPOSE 5010
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

