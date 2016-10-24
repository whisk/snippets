const cp = require('child_process');

cp.exec('ls -la', function(ret, stdout, stderr) {
  if (ret) {
    console.log("Error code:", ret);
  }
  console.log("STDOUT:", stdout);
  if (stderr)
    console.log("STDERR:", stderr);
});