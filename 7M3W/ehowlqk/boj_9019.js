const fs = require("fs");
const input = fs
  .readFileSync("./7M3W/ehowlqk/boj_9019.txt")
  .toString()
  .split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (idx; idx < T + 1; idx++) {
  const [a, b] = input[idx].split(" ").map((e) => Number(e));

  const visited = Array(10000).fill(false);
  visited[a] = true;

  const q = [[a, ""]];

  while (q.length) {
    const [num, curr] = q.shift();

    if (num === b) {
      console.log(curr);
      break;
    }

    for (const [next, cmd] of [
      [D(num), "D"],
      [S(num), "S"],
      [L(num), "L"],
      [R(num), "R"],
    ]) {
      if (visited[next] === false) {
        q.push([next, curr + cmd]);
        visited[next] = true;
      }
    }
  }
}

function D(n) {
  return (n * 2) % 10000;
}

function S(n) {
  return n === 0 ? 9999 : (n - 1) % 10000;
}

function L(n) {
  return (n % 1000) * 10 + Math.floor(n / 1000);
}

function R(n) {
  return (n % 10) * 1000 + Math.floor(n / 10);
}
