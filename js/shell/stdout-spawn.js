const spawn = require('child_process').spawn;

var p = spawn('ls', ['-la']);

p.stdout.on('data', (data) => {
  console.log('stdout:', data.toString());
});

p.stderr.on('data', (data) => {
  console.log('stderr:', data.toString());
});

p.on('close', (code) => {
  console.log(`Process exited with code ${code}`);
});