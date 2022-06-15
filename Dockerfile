FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY rede_social/app.py /app.py
COPY rede_social/business/Rede.py business/Rede.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
