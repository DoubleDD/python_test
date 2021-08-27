#!/bin/bash

time=$(date "+%Y-%m-%d_%H-%M-%S")
filename=result/$time.json

curl -X GET \
"http://172.30.13.177:30013/x-data-resource-service/v1/resources/data-provider/\
om_region?columns=code%2Cregion_code%2Cregion_name%2Cregion_path&filter=1%3D1" \
-H "accept: application/json;charset=UTF-8" \
-H "x-token: eyJ1c2VyIjoiY2NiZmVkYzgwMTYzYzAwN2IxNjkzZjlmYzgxYWU1MjMiLCJ1c2VyTmFtZSI6IueuoeeQhuWRmCIsIm9yZ2FuaXphdGlvbk5hbWUiOiLkupHnspLmmbrmhaciLCJleHBpcmVkX3RpbWUiOiIyMDIwLTEwLTIxIDA1OjMwOjEwIiwic2lnbmF0dXJlIjoiUW1ncWM2Y3FEcVZPRjJZeWZMdTAzMGY5NkFoV2VHNVQycHF5blk1eHNULTlUMUlGOWF2NEZJQUktWjR0RElkcUF3OXpWWERzUVV3bm54MFEwbkJ1WmpTczJMQWNPNHNsYl96ZEl0UWRjVHJJbFJuaHY4LW9QYXZtLTR4cHhyQy03SWV1MXR2MlVTVWhBV3E4dFUzTWRfNGI0VVdDZ00waHlId3dkV3ltMmVJPSJ9"\
 > $filename

echo $filename
