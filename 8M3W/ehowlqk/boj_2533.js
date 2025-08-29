const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./boj_2533.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
const edges = Array.from({ length: n + 1 }, () => []);
for (let i = 1; i < n; i++) {
  const [a, b] = input[i].split(" ").map((e) => Number(e));
  edges[a].push(b);
  edges[b].push(a);
}

const visited = Array(n + 1).fill(false);
function dp(node) {
  visited[node] = true;
  let notEA = 0,
    isEA = 1;
  for (let child of edges[node]) {
    if (visited[child]) continue;
    const result = dp(child);
    notEA += result[1];
    isEA += Math.min(...result);
  }
  return [notEA, isEA];
  // [얼리어답터 아닐때, 얼리어답터일때]
}

console.log(Math.min(...dp(1)));
