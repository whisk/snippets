import re

def parse_ini(fname, section):
  f = open(fname, 'r')
  data = dict()
  required_section = False
  for line in f:
    if line.lstrip().find('[') == 0:
      if line.lstrip().lower().find('[%s]' % section) == 0:
        required_section = True
      else:
        required_section = False

    if required_section:
      m = re.search('(\w+?)=(\S+)', line)
      if m:
        data[m.group(1)] = m.group(2)

  return data

if __name__ == '__main__':
  print(parse_ini('sample.ini', 'client'))