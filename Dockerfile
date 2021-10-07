FROM koala21/kampangbot:buster

RUN git clone -b FahriUserBot https://github.com/fahrial2310/Fahri-UserBot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/fahrial2310/Fahri-UserBot/blob/FahriUserBot/requirements.txt

CMD ["python3","-m","FahriUserBot"]
