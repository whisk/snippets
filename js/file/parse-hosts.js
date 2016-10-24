'use strict';

const fs = require('fs');

function parseHosts(hosts, pattern, callback) {
  fs.readFile(hosts, (err, data) => {
    if (err) {
      throw err;
    }
    let hosts = [];
    for (let line of data.toString().split(/\n/)) {
      line = line.trim();
      if (line[0] == '#' || line.length == 0)
        continue;
      let entries = line.split(/\s+/);
      let ip = entries.shift();
      if (!ip.match(/^\d+\.\d+\.\d+\.\d+$/) && !ip.match(/:/)) { // hack for ipv6
        console.log('Invalid IP:', ip);
      }
      for (let h of entries) {
        if (h.match(pattern)) {
          hosts.push(h);
        }
      }
    }
    callback(hosts);
  });
}

parseHosts('/etc/hosts', 'wv', (hosts) => {
  console.log(hosts);
});