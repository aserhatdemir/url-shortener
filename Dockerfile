FROM python:3.7.1

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "web.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True


RUN mkdir /app
WORKDIR /app


ADD . /app
RUN pip install -r /app/requirements.txt


EXPOSE 5000


CMD flask run --host=0.0.0.0