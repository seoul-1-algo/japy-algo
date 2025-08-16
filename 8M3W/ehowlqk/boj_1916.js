const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M3W/ehowlqk/boj_1916.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

let idx = 0;

n = Number(input[idx++]);
m = Number(input[idx++]);

const edges = [];
for (idx; idx < m + 2; idx++) {
  edges.push(input[idx].split(" ").map((e) => Number(e)));
}
const [start, end] = input[idx].split(" ").map((e) => Number(e));
console.log(start, end);

const heap = []

