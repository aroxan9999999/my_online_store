FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY dist/diploma-frontend-0.6.tar.gz /app/
RUN pip install /app/diploma-frontend-0.6.tar.gz
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "127.0.0.1:7000"]
