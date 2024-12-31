FROM python:3.13.1

RUN apt update && apt upgrade -y \
    wget \
    curl \
    unzip


RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

RUN wget https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.204/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN mv ./chromedriver-linux64/chromedriver /usr/local/bin/

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "wellhub/main.py"]