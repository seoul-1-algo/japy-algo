const fs = require("fs");
const input = fs
  .readFileSync("./8M1W/ehowlqk/boj_11403.txt")
  .toString()
  .split("\n");

const n = Number(input[0]);

const graph = input
  .slice(1, n + 1)
  .map((str) => str.split(" ").map((e) => Number(e)));

for (let k = 0; k < n; k++) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const edges = [graph[i][k], graph[k][j]];
      graph[i][j] = edges[0] * edges[1] ? 1 : graph[i][j];
    }
  }
}

graph.forEach((row) => console.log(...row));
