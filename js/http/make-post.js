'use strict';

const http = require('http');
const url = require('url');

function makePost(req_url, req_body, callback) {
  let options = url.parse(req_url);
  options.method = 'POST';
  let req = http.request(options, (res) => {
    var body = '';
    res.on('data', (data) => {
      body += data.toString();
    });
    res.on('end', () => {
      try {
        let json_body = JSON.parse(body);
        callback(json_body);
      } catch (e) {
        console.log('Error parsing response:', e);
      }
    });
  });
  req.write(req_body);
  req.end();
}

makePost('http://localhost:8000', 'TESTBODY', (json_body) => {
  console.log(json_body);
});