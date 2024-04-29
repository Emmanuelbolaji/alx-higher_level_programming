#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /tmp/response_body -w "%{http_code}" "$1" > /dev/null && grep -q "200" /tmp/response_body && tail -n +2 /tmp/response_body rm /tmp/response_body
