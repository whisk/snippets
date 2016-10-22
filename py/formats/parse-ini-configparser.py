import configparser

def parse_ini(fname, section):
  config = configparser.ConfigParser()
  config.read(fname)
  try:
    return dict(config[section].items())
  except KeyError:
    return {}

if __name__ == '__main__':
  data = parse_ini('sample.ini', 'Client')
  print('user:', data.get('user', '[not set]'))
  print('password:', data.get('password', '[not set]'))