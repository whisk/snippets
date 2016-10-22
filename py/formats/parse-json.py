import json

def get_dependencies(fname, section = 'dependencies'):
  try:
    data = json.load(open(fname))
    return list(data.get(section).keys())
  except AttributeError:
    return []

if __name__ == '__main__':
  print(get_dependencies('sample.json'))