'use strict';

function parse_version(ver_string) {
  let patt = new RegExp(/^(\d+)(?:\.(\d+)(?:\.(\d+)(?:-(\w+))?)?)?$/);
  let m = ver_string.match(patt);
  if (m) {
    return {
      major: m[1],
      minor: m[2],
      patch: m[3],
      build: m[4]
    };
  } else {
    return false;
  }
}

console.log(parse_version(process.argv[2].toString()));