#!/usr/bin/env python3

import urllib.request
import json
import sys

def make_post(url, post_body):
  try:
    res = urllib.request.urlopen(url, post_body.encode())
    text = ''
    for line in res.readlines():
      text += line.decode()
    print('raw body:', text)
    print(json.loads(text))
  except json.decoder.JSONDecodeError as e:
    print(e)
    sys.exit(1)
  except urllib.error.HTTPError as e:
    print(e)
    sys.exit(1)

if __name__ == '__main__':
  make_post(sys.argv[1], sys.argv[2])