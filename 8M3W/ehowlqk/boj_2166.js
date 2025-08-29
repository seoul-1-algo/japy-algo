const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M3W/ehowlqk/boj_2166.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const n = Number(input[0]);
const coors = input
  .slice(1)
  .map((arr) => arr.split(" ").map((num) => Number(num)));

let sumCross = 0;

for (let i = 0; i < n; i++) {
  const [x1, y1] = i ? coors[i] : coors[0];
  const [x2, y2] = i ? coors[i - 1] : coors[n - 1];
  sumCross += x1 * y2 - x2 * y1;
}

console.log((0.5 * Math.abs(sumCross)).toFixed(1));
