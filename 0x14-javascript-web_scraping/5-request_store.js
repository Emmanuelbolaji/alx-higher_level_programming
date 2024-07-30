#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const apiUrl = process.argv[2];
const filePath = process.argv[3];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching URL:', error);
  } else if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
