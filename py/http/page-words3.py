#!/usr/bin/env python3

import urllib.request
import re

def count_page_words(url, pattern):
  cnt = 0
  for line in urllib.request.urlopen(url).readlines():
    if re.search(pattern, line.decode()):
      cnt += 1
  return cnt

if __name__ == '__main__':
  print(count_page_words('https://inventos.ru', 'video'))
