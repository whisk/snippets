import sys
import re

def check_email(email):
  m = re.match('^([0-9a-z_]+[0-9a-z_+.]*)@([0-9a-z_]+[0-9a-z_+.]*\.[0-9a-z]+)$', email, re.I)
  if m:
    return (m.group(1), m.group(2)) # username and domain
  else:
    return None

if __name__ == '__main__':
  print(check_email(sys.argv[1]))