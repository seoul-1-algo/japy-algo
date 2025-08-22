const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M3W/ehowlqk/boj_2239.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.split("").map((num) => Number(num)));

console.log(input);

function row() {}
function col() {}
function block() {}
