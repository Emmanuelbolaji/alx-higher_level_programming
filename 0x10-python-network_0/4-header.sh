#!/bin/bash
# This script takes in a URL as an argument, sends a GET request with a header X-School-User-Id: 98, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
