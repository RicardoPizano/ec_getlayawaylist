FROM python:3.9.13-slim-buster

WORKDIR /ec_mscomics

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV MONGO_URL=""
ENV USERS_BASE_URL=""

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]