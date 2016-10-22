import sys
import re

def parse_version(ver_string):
  m = re.match('^(?P<major>\d+)(?:\.(?P<minor>\d+)(?:\.(?P<patch>\d+)(?:-(?P<build>\w+))?)?)?$', ver_string)
  if m:
    return m.groupdict()
  else:
    return None

if __name__ == '__main__':
  print(parse_version(sys.argv[1]))