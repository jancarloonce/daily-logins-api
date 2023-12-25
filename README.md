
REST API application is done using Flask Framework and the database used is Elasticsearch
both are hosted on AWS. Flask on EC2 instance while Elasticsearch is on Elastic Beanstalk.


A rough diagram shows the flow and tech stack:

![alt text](https://github.com/jancarloonce/th-exam-jancarloonce11/blob/main/diagram.png)

# AWS Hosted Service

You can try it LIVE here: http://3.25.177.132:8080/users/


## Installs the needed packages

    pip install -r /Part2/requirements.txt

## Run the app

    python app.py

# REST API

The REST API to the Daily check-ins is described below.

## Get ALL data

### Request

`GET /users/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/users


### Response

    HTTP/1.1 201 Created
    Date: Sun, 22 Oct 2023 12:36:30 GMT
    Status: 201 Created
    Connection: close
    Content-Type: application/json
    Location: /thing/1
    Content-Length: 36

    {
      "total_rows": 20000,
      "rows": [
        {
          "user": "robert",
          "timestamp": "2019-09-27 00:00:00+00:00",
          "hours": "8.0",
          "project": "bizdev"
        },

        ...


## Get specific user by supplying url parameters

### Request

`GET /users/user?=jon`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/users?user=jon

### Response

    HTTP/1.1 200 OK
    Date: Sun, 22 Oct 2023 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 36

    {
    "total_rows": 372,
    "rows": [
        {
            "user": "jon",
            "timestamp": "2018-11-22 11:36:11.042000+00:00",
            "hours": "1.0",
            "project": "project-25"
        },
        {
            "user": "jon",
            "timestamp": "2018-11-22 11:36:11.042000+00:00",
            "hours": "2.25",
            "project": "project-25"
        },

        ....

