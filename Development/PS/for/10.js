const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let number = Number(input[0]);

let result = "";

for (let i = 1; i <= number; i++) {
  for (let j = number - i; j > 0; j--) {
    result += " ";
  }
  for (let j = 1; j <= i; j++) {
    result += "*";
  }
  result += "\n";
}
console.log(result);
