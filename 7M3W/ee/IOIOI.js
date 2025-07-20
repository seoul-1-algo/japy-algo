const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./5525.txt";

const input = fs.readFileSync(filePath).toString().trim().split('\n');

const N = parseInt(input[0]);
const M = parseInt(input[1]);
const chars = input[2];

let cnt = 0;
let cur = 0;

for (let i = 0; i < M; i++) {
  let temp = (cur % 2 === 0) ? 'I' : 'O';

  if (chars[i] === temp) {
    cur += 1;

    if (cur === 2 * N + 1) {
      cnt += 1
      cur = 2 * N - 1
    }
  } else {
    cur = (chars[i] === 'I') ? 1 : 0
  }
}

console.log(cnt)