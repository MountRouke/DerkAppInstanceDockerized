FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
    curl unzip libgconf-2-4 \
    xvfb chromium

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY start.sh ./
RUN chmod +x start.sh

EXPOSE 8789
ENV DERK_CHROME_EXECUTABLE chromium

CMD ["/start.sh"]