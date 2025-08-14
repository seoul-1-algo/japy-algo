const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M2W/ehowlqk/boj_9251.txt";
const [A, B] = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((e) => e.split(""));

const dp = Array.from({ length: A.length + 1 }, () =>
  Array(B.length + 1).fill(0)
);

for (let i = 1; i < A.length + 1; i++) {
  for (let j = 1; j < B.length + 1; j++) {
    if (A[i - 1] === B[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
    else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
  }
}

console.log(dp.reduce((max, row) => Math.max(max, ...row), -Infinity));
