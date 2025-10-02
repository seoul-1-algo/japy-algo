const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_2467.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const n = Number(input[0]);
const pHVals = input[1]
  .split(" ")
  .map((num) => Number(num))
  .sort((a, b) => a - b);

let start = 0,
  end = n - 1;
let selected = [pHVals[start], pHVals[end]];
while (start < end) {
  const mixed = pHVals[start] + pHVals[end];
  if (
    Math.abs(pHVals[start] + pHVals[end]) < Math.abs(selected[0] + selected[1])
  ) {
    selected = [pHVals[start], pHVals[end]];
  }

  if (mixed < 0) start++;
  else if (mixed > 0) end--;
  else break;
}

console.log(selected[0], selected[1]);
