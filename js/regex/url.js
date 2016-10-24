'use strict';

function check_url(url) {
  let patt = new RegExp(/^(\w+):\/\/([0-9a-z.]+)(:\d+)?(?:\/([0-9a-z_\/.]+)?(\S+)?)?$/);
  let m = url.match(patt);
  if (m) {
    let schema = m[1];
    let port = m[3];
    if (port == null && schema == 'http')
      port = 80;
    return {'schema': schema, 'hostname': m[2], 'port': port, 'path': m[4], 'qs': m[5]};
  }
}

console.log(check_url(process.argv[2].toString()));