import sys

def read_users(fname = '/etc/passwd', min_uid = 200):
  res = []
  for line in open(fname):
    try:
      l = line.split(':')
      u, uid = l[0], int(l[2])
      if uid > min_uid:
        res.append(u)
    except Exception as e:
      sys.stderr.write("Error on line %s: %s\n" % (line, e))
      pass

  return res

def save_users(users, fname):
  if len(users) == 0:
    return None
  with open(fname, 'w') as f:
    for u in users:
      f.write(u + "\n")

if __name__ == '__main__':
  try:
    save_users(read_users(), 'users.txt')
  except Exception as e:
    sys.stderr.write(e + "\n")
    sys.exit(1)
