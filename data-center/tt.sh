#!/bin/bash

time=$(date "+%Y-%m-%d_%H-%M-%S")
filename=result/$time.json

curl -X GET \
"http://172.30.13.177:30013/x-data-resource-service/v1/resources/data-provider/\
om_region?columns=code%2Cregion_code%2Cregion_name%2Cregion_path&filter=1%3D1" \
-H "accept: application/json;charset=UTF-8" \
-H "x-token: eyJ1c2VyIjoiY2NiZmVkYzgwMTYzYzAwN2IxNjkzZjlmYzgxYWU1MjMiLCJ1c2VyTmFtZSI6IueuoeeQhuWRmCIsIm9yZ2FuaXphdGlvbk5hbWUiOiLkupHnspLmmbrmhaciLCJleHBpcmVkX3RpbWUiOiIyMDIwLTEwLTIwIDEwOjQ3OjI0Iiwic2lnbmF0dXJlIjoiS3RfRFdKTy1rVm5DdTJSLUNQak5ZamVKZmQxUmxDc0x6ajZCQVdmQldTTF9CMTMwSGMtMVNxSlRJQUxJOXFxZ3dmdnFTY25pMXgxUVBFWmZXejVhd1RIdTFLMzY1VEUyVW02c3ZQVHpaSVdyUzRCUDUzdUQtQzRNR3BQdk5lM053UkJtZlp6bC1uTzFrMmZBZGFKRFRwUWN3cEFpdk9FYmlDMXQwYzcwNXd3PSJ9"\
 > $filename

echo $filename
