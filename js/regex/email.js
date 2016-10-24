'use strict';

function check_email(email) {
  return email.match(/^([0-9a-z_]+[0-9a-z_+.]*)@([0-9a-z_]+[0-9a-z_+.]*\.[0-9a-z]+)$/) !== null;
}

console.log(check_email(process.argv[2].toString()));