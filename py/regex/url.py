import sys
import re

def check_url(url):
  patt = '^(\w+)://([0-9a-z.]+)(:\d+)?(?:/([0-9a-z_/.]+)?(\S+)?)?$'
  m = re.match(patt, url, re.I)
  if m:
    schema = m.group(1)
    port = m.group(3)
    if port is None and schema == 'http':
      port = 80
    return {'schema': schema, 'hostname': m.group(2), 'port': port, 'path': m.group(4), 'qs': m.group(5)}
  else:
    return None

if __name__ == '__main__':
  print(check_url(sys.argv[1]))