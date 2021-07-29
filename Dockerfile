FROM python:3.6

ADD . /

WORKDIR /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies:
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . /

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
