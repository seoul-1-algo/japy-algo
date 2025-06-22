function findKevinBacon(i, edges) {
  const visited = Array(n).fill(10000);
  visited[i] = 0;
  const kevinBacon = dfs(i + 1, 0, edges, visited);
  return kevinBacon.reduce((a, b) => a + b);
}

function dfs(member, depth, edges, visited) {
  edges[member - 1].forEach((friend) => {
    if (visited[friend - 1] > depth + 1) {
      visited[friend - 1] = depth + 1;
      visited = dfs(friend, depth + 1, edges, visited);
    }
  });

  return visited;
}

const fs = require("fs");
const input = fs
  .readFileSync("./6M4W/ehowlqk/boj_1389.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map(Number);

const edges = Array.from({ length: n }, () => []);

// 인접 배열
for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  edges[a - 1].push(b);
  edges[b - 1].push(a);
}

let answer = 0;
let minKevinBacon = 1000;

for (let i = 0; i < n; i++) {
  const kevinBacon = findKevinBacon(i, edges);
  if (minKevinBacon > kevinBacon) {
    answer = i + 1;
    minKevinBacon = kevinBacon;
  }
}

console.log(answer);
