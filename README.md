issueTracking
=============

An Issue Tracking System project for college using Django, Python and Bootstrap

The project is live on [issuetrackingsystem.herokuapp.com](http://issuetrackingsystem.herokuapp.com/)

## Pre requisites
- A local/remote postgres installation with a valid username/password and preexisting empty database

## Setup on local
- Use virtualenv to setup a python3 environment
- Install required dependencies using `pip3 install -r requirements.txt`
- Modify the following values in `issueTracking/settings.py` to test the website on localhost:
    - `SECURE_SSL_REDIRECT`
    - `SECURE_HSTS_INCLUDE_SUBDOMAINS`
    - `SECURE_HSTS_PRELOAD`
    - `DEBUG`
- Following environment variables are necessary for the commands below to execute successfully
    - `DJANGO_SECRET_KEY`
    - `DATABASE_URL`
- Run migrations if required
  ```
  python3 manage.py migrate
  ```
- Run debug server
  ```
  python3 manage.py runserver
  ```