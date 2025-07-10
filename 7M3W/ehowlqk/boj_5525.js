const fs = require("fs");
const input = fs
  .readFileSync("./7M3W/ehowlqk/boj_5525.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input.slice(0, 2).map((e) => Number(e));
const S = input[2];

let answer = 0;
let start = false;
let prev = "";
let len = 0;

for (const letter of S) {
  // I: P(len) 시작
  if (letter === "I") {
    if (!start) {
      start = true;
    } else {
      // 이전이 O일 경우: P(len) -> P(len+1)
      if (prev === "O") {
        ++len;
        // len이 n보다 클 때 -> P(n) 하나씩 추가
        if (len >= N) {
          answer++;
        }
      }
      // 이전이 I인 경우: len 초기화
      else {
        len = 0;
      }
    }
    prev = "I";
  } else {
    // O: 이전도 O였다면 P(len) 종료, len 초기화
    if (prev === "O") {
      start = false;
      len = 0;
    }
    prev = "O";
  }
}

console.log(answer);
