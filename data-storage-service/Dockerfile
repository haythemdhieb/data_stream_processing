FROM python:3.7
ENV PATH /usr/src/app/bin:$PATH


WORKDIR /app
COPY . .

RUN  pip install -r requirements.txt



CMD ["python","main.py"]