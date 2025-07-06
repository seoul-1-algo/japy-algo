const fs = require("fs");
const input = fs
  .readFileSync("./6M4W/ehowlqk/boj_30804.txt")
  .toString()
  .trim()
  .split("\n");

let start = 0;
let end = 1;

const fruits = input[1].split(" ").map(Number);

let tanghuru = new Map();
tanghuru.set(fruits[0], 1);

let answer = 1;
while (end < Number(input[0])) {
  if (tanghuru.size < 3) {
    tanghuru.set(fruits[end], (tanghuru.get(fruits[end]) || 0) + 1);
    end++;
    if (tanghuru.size < 3) {
      answer = Math.max(answer, end - start);
    }
  } else {
    if (tanghuru.get(fruits[start]) > 1) {
      tanghuru.set(fruits[start], tanghuru.get(fruits[start]) - 1);
    } else {
      tanghuru.delete(fruits[start]);
    }
    start++;
  }
}

console.log(answer);
