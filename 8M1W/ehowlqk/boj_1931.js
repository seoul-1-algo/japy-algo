const fs = require("fs");
const input = fs
  .readFileSync("./8M1W/ehowlqk/boj_1931.txt")
  .toString()
  .trim()
  .split("\n");

let idx = 0;

const n = Number(input[idx++]);
const meetingTime = [];
for (idx; idx <= n; ++idx) {
  meetingTime.push(input[idx].split(" ").map((e) => Number(e)));
}
meetingTime.sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1])); // 끝나는 시간 기준 오름차순 정렬

console.log(meetingTime);

let prevEnd = 0, // 이전 회의의 종료 시간
  answer = 0; // 출력할 답
for (const [start, end] of meetingTime) {
  // 시작 시간이 이전 회의의 종료시간 이후라면 정답에 포함한다.
  if (start >= prevEnd) {
    prevEnd = end;
    ++answer;
  }
}

console.log(answer);
