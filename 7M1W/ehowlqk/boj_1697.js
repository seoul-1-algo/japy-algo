const fs = require("fs");
const [n, m] = fs
  .readFileSync("./7M1W/ehowlqk/boj_1697.txt")
  .toString()
  .split(" ");

const visited = Array(100001).fill(1e9);
let destination = [Number(n)];
let cost = 0;
while (cost < 100001) {
  if (destination.includes(Number(m))) {
    break;
  }
  const tmp = new Array();
  destination.forEach((e) => {
    if (e < 100001 && visited[e] > cost) {
      visited[e] = cost;
      if (e > 0) {
        tmp.push(e - 1);
      }
      if (e < 100000) {
        tmp.push(e + 1);
      }
      if (e * 2 < 100001) {
        tmp.push(e * 2);
      }
    }
  });

  destination = tmp;
  cost++;
}

console.log(cost);
