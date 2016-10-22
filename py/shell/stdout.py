from subprocess import check_output

print(check_output(['ls', '-la']).decode())