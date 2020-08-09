FROM sandy1709/catuserbot:latest

#clonning repo 
RUN git clone -b Jisan09-Test https://github.com/Jisan09/catuserbot.git /root/userbot
#working directory 
WORKDIR /root/userbot
ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
