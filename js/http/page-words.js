'use strict';

const http = require('http');

function pageWords(url, word, callback) {
  var req = http.request(url, (res) => {
    var body = '';
    res.on('data', (data) => {
      body += data.toString();
    });
    res.on('end', () => {
      var patt = new RegExp(word, 'g');
      var cnt = 0;
      while (patt.exec(body) !== null) {
        cnt += 1;
      }
      callback(cnt);
    });
  });
  req.end();
}

pageWords('http://inventos.ru', 'video', (cnt) => {
  console.log(cnt);
});