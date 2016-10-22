import csv

def get_top(fname, threshold=0):
  top = [None, -1]
  with open(fname) as csv_file:
    for row in csv.reader(csv_file):
      try:
        if int(row[1]) >= threshold and top[1] <= int(row[2]):
          top = [row[0], int(row[2])]
      except IndexError:
        pass

  return top

if __name__ == '__main__':
  print(get_top('sample.csv', 10))