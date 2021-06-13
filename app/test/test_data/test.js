const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
 

let input;
readline.question('', name => {
  input = name.split(" ");
  readline.close();
  main();
});

function main(){
  console.log(input[0] ** input[1])
}