FROM python:3.7

RUN mkdir -p /opt/services/workolist/src
WORKDIR /opt/services/workolist/src

# use --system flag because we don't need an extra virtualenv
COPY Pipfile Pipfile.lock /opt/services/workolist/src/
RUN pip install pipenv && pipenv install --dev --system

COPY . /opt/services/workolist/src

EXPOSE 8000

COPY ./bin/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
