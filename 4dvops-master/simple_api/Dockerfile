FROM python:2.7-stretch
LABEL maintainer="223689@supinfo.com"
COPY ./simple_api/student_age.py /
COPY ./simple_api/student_age_test.py /
COPY ./simple_api/student_age.json /
RUN apt-get update -y && apt-get install python-dev python3-dev libsasl2-dev python-dev libldap2-dev libssl-dev -y
RUN pip install flask flask_httpauth flask_simpleldap python-dotenv

EXPOSE 5000
CMD [ "python", "./student_age.py" ]