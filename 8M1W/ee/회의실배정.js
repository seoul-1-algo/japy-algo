const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./1931.txt";

const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = parseInt(input[0]);
const conferences = []

for (let i = 1; i <= N; i++) {
  const [start, end] = input[i].split(' ').map(Number);
  conferences.push([start, end]);
}

conferences.sort((a, b) => {
  if (a[1] === b[1]) { // 시작시간과 끝나는 시간이 같으면
    return a[0] - b[0] // 시작시간 오름차 순
  }
  return (a[1] - b[1]); // 끝나는 시간 오름차 순
})

let cnt = 0;
let prevEnd = 0;

for (const [curStart, curEnd] of conferences) {
  // 이전 회의가 아직 안 끝났으면
  if (prevEnd > curStart) {
    continue
  }

  // 이전 회의가 끝났으면
  prevEnd = curEnd
  cnt++;
}

console.log(cnt)