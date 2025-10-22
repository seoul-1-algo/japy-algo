const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1806.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, s] = input[0].split(" ").map((e) => Number(e));
const arr = input[1].split(" ").map((e) => Number(e));

let answer = n + 1;
let sum = arr[0];
let start = 0,
  end = 0;

while (start <= end && end < n) {
  // 조건 만족하는 경우
  if (sum >= s) {
    // 만약 현재 길이가 더 짧다면 정답 갱신
    if (end - start + 1 < answer) {
      answer = end - start + 1;
    }
    sum -= arr[start];
    ++start;
  } else {
    ++end;
    sum += arr[end];
  }
}

console.log(answer <= n ? answer : 0);
