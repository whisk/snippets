import sys
import re

def read_hosts(fname, pattern):
  found = []
  for line in open(fname, 'r'):
    line = line.strip()
    if len(line) == 0 or line[0] == '#':
      continue
    ip, names = re.split('\s+', line, 1)
    if not re.match('^\d+\.\d+\.\d+\.\d+$', ip) and not re.search(':', ip):
      # dirty trick for ipv6
      raise ValueError("Invalid IP: %s" % ip)
    if names is None or len(names) == 0:
      raise ValueError("No host name for IP %s" % ip)
    name = names.split()[0]
    if re.search(pattern, name):
      found.append(name)
  return found

if __name__ == '__main__':
  print(read_hosts('/etc/hosts', sys.argv[1]))
