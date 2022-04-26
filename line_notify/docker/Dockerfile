FROM python:3.8.13


#Use root to install the related package
USER root

#Setting timezone
ENV TZ Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#Construct the home directory and work directory
RUN addgroup --gid 1001 app 
RUN useradd -u 1001 \
            -G app \
            -d /home/app/workdir \
            -s /sbin/nologin \
            -g app \
            app

#Install python, Set timezone and relation 
RUN apt-get update \
    && apt-get install tzdata \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get install -y \
    linux-libc-dev \
    python3-pip \
    libyaml-cpp-dev \
    libyaml-dev \
    libsm6 libxext6 libxrender-dev libfreetype6 libssl1.1 openssl \
    ffmpeg \
    protobuf-compiler \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#Create an app user for the application usage
ENV HOME=/home/app
ENV APP_HOME=/home/app/workdir

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
RUN chown -R app:app $APP_HOME

#Install python packages
COPY ./requirements.txt $APP_HOME/requirements.txt
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 --no-cache-dir install -r $APP_HOME/requirements.txt

#Project data and code
# ALL FILE Into image: COPY . /home/app/workdir/
COPY ./main.py $APP_HOME/main.py
COPY ./config $APP_HOME/config/

# Opencv package need dconf folder to save the information.
RUN mkdir -p /home/app/.cache/dconf
RUN mkdir -p $APP_HOME/data/logs
RUN chmod a+w /home/app/.cache/dconf
RUN chmod a+w -R $APP_HOME/data
ENV PROJECT_PATH=$APP_HOME

RUN usermod -a -G video app

#Change User - app
USER app

#Run api code
ENTRYPOINT [ "/bin/bash" , "-c" , "python3 -W ignore main.py"]