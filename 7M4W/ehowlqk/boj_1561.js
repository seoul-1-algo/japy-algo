const fs = require("fs");
const input = fs
  .readFileSync("./7M4W/ehowlqk/boj_1561.txt")
  .toString()
  .split("\n");

const [n, m] = input[0].split(" ").map((e) => Number(e)); // n: 사람 수, m: 놀이기구 수

const times = input[1].split(" ").map((e) => Number(e)); // 운행시간

function binarySearch(n) {
  let start = 1,
    end = n * 30;
  while (start < end) {
    const mid = Math.ceil((start + end) / 2);
    const result = sumPeople(mid);
    if (result < n) start = mid;
    else end = mid - 1;
  }
  return start;
}

function sumPeople(mid) {
  let result = 0;
  times.forEach((time) => {
    result += Math.ceil(mid / time);
  });
  return result;
}

function solution(n, m) {
  if (n <= m) return n;
  const theTime = binarySearch(n);
  let tmp = sumPeople(theTime);
  const timesLeft = [];
  for (let i = 0; i < m; i++) {
    const timeLeft = theTime % times[i];
    if (timeLeft === 0) timesLeft.push(i + 1);
  }
  return timesLeft[n - tmp - 1];
}

console.log(solution(n, m));
