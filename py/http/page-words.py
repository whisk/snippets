#!/usr/bin/env python2
import urllib
import re

def count_page_words(url, pattern):
  cnt = 0
  for line in urllib.urlopen(url).readlines():
    if re.search(pattern, line):
      cnt += 1
  return cnt

if __name__ == '__main__':
  print(count_page_words('https://inventos.ru', 'video'))
