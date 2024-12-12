FROM python:3.10-alpine

WORKDIR /code

RUN apk update && apk add --no-cache chromium \
    chromium-chromedriver

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/index.py", "--port", "80", "--proxy-headers"]