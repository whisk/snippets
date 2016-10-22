import xml.etree.ElementTree as et

def get_baseurls(fname):
  data = et.parse(fname)
  res = []
  # note the namespace!
  for url in data.getroot().findall('.//{urn:mpeg:DASH:schema:MPD:2011}BaseURL'):
    res.append(url.text)
  return res

if __name__ == '__main__':
  print(get_baseurls('sample.xml'))