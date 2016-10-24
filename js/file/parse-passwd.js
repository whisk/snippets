'use strict';
const fs = require('fs');

function getUsers(callback) {
  fs.readFile('/etc/passwd', (err, data) => {
    if (err) {
      throw err;
    }
    let users = [];
    for (let line of data.toString().split(/\n/)) {
      try {
        let entry = line.split(/:/);
        if (parseInt(entry[2]) > 200) {
          users.push(entry[0]);
        }
      } catch (e) {
        console.log(`Error parsing line ${line}: ${e}`);
      }
    }
    callback(users);
  });
}

getUsers((users) => {
  console.log(users);
});