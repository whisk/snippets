from subprocess import Popen, PIPE

try:
  p = Popen(["ls", "-la"], stdout=PIPE)
  p.wait()
  if p.returncode == 0:
    print(p.stdout.read().decode())
  else:
    print('Error:', p.stderr.read().decode())
except OSError as e:
  print('OSError:', e)
