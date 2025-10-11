const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_9935.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const text = input[0];
const bomb = input[1];
const stack = [];
for (let letter of text) {
  stack.push(letter);
  if ("".concat(...stack.slice(-bomb.length)) === bomb) {
    for (let i = 0; i < bomb.length; i++) stack.pop();
  }
}

console.log(stack.length ? stack.join("") : "FRULA");
