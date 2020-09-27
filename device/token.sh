#!/bin/bash

curl 'http://localhost:10003/api/uaa/oauth/token' \
  -H 'Accept: application/json' \
  -H 'Authorization: Basic YnJvd3Nlcjo=' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://localhost:8000' \
  -H 'Referer: http://localhost:8000/mscode/user/login' \
  --data-raw 'tenantCode=10004&username=admin&password=666888&type=account&scope=ui&grant_type=password&client_id=browser'
