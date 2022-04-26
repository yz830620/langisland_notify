FROM service-line-notify

USER root

ENV APP_HOME=/home/app/workdir
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY ./docker/tests/requirements-test.txt $APP_HOME/requirements.txt
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 --no-cache-dir install -r $APP_HOME/requirements.txt

COPY ./config/ $APP_HOME/config/
COPY ./tests/ $APP_HOME/tests/
COPY ./src/ $APP_HOME/src/
COPY ./main.py $APP_HOME/main.py
ENV PROJECT_PATH=$APP_HOME
ENV PYTHONPATH=$APP_HOME

ENTRYPOINT [ "/bin/bash" , "-c" , "pytest -q -p no:warnings -o log_cli=true --capture=no tests/"]