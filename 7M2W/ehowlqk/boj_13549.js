const fs = require("fs");
const [N, M] = fs
  .readFileSync("./7M2W/ehowlqk/boj_13549.txt")
  .toString()
  .trim()
  .split(" ")
  .map((e) => parseInt(e));

const range = 100001;

if (N >= M) {
  console.log(N - M);
} else {
  const visited = new Array(range).fill(200000);
  let curr = [];
  for (let i = N; i < range; i *= 2) {
    if (i === M) {
      console.log(0);
      return;
    }
    visited[i] = 0;
    curr.push(i);
    if (i == 0) {
      break;
    }
  }
  let cost = 1;
  while (1) {
    // 이동
    let next = [];

    while (curr.length) {
      let loc = curr.pop();
      for (const move of [loc + 1, loc - 1]) {
        if (move === M) {
          console.log(cost);
          return;
        }
        if (0 <= move < range && visited[move] > cost) {
          visited[move] = cost;
          next.push(move);
        }
      }
    }

    // 순간이동
    for (let loc of next) {
      if (loc === 0) {
        continue;
      }
      for (let i = loc; i < range; i *= 2) {
        if (loc === M) {
          console.log(cost);
          return;
        }
        if (visited[i] > cost) {
          visited[i] = cost;
          next.push(i);
        }
      }
    }

    curr = [...next];
    cost++;
  }
}
