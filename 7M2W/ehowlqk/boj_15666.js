const fs = require("fs");
const input = fs
  .readFileSync("./7M2W/ehowlqk/boj_15666.txt")
  .toString()
  .split("\n");

let idx = 0;

const [n, m] = input[idx++].split(" ").map((e) => parseInt(e));

const nums = [
  ...new Set(
    input[idx++]
      .split(" ")
      .map((e) => parseInt(e))
      .sort((a, b) => a - b)
  ),
];

const answer = [];

function solution(curr, depth) {
  if (depth === m) {
    return answer.push(curr);
  }
  for (let i = 0; i < nums.length; i++) {
    if (!curr.length || nums[i] >= curr[curr.length - 1]) {
      solution([...curr, nums[i]], depth + 1);
    }
  }
}

solution([], 0);
answer.forEach((comb) => console.log(...comb));
