const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_5639.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((e) => Number(e));

function gndnl(start, end) {
  if (start >= end) return;
  let mid = end;
  for (let i = start; i < end; i++) {
    if (input[i] > input[start]) {
      mid = i;
      break;
    }
  }

  gndnl(start + 1, mid);
  gndnl(mid, end);
  console.log(input[start]);
}

gndnl(0, input.length);
