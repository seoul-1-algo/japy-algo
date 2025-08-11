const fs = require("fs");
const input = fs
  .readFileSync("./8M2W/ehowlqk/boj_14940.txt")
  .toString()
  .trim()
  .split("\n");

const [n, m] = input[0].split(" ").map((e) => Number(e));

const graph = [],
  start = [];

for (let row = 1; row < n + 1; row++) {
  const tmp = input[row].split(" ").map((e) => 0 - Number(e));
  graph.push(tmp); // graph 복사
  const col = tmp.indexOf(-2); // 시작 지점인지 확인
  if (col !== -1) start.push(row - 1, col); // 시작 지점: row - 1, col
}

const dr = [1, -1, 0, 0],
  dc = [0, 0, 1, -1];

const q = [];
q.push([start, 0]);
graph[start[0]][[start[1]]] = 0;

while (q.length) {
  const [[r, c], cost] = q.shift();

  for (i = 0; i < 4; i++) {
    const nr = r + dr[i],
      nc = c + dc[i];

    if (0 <= nr && nr < n && 0 <= nc && nc < m && graph[nr][nc] < 0) {
      q.push([[nr, nc], cost + 1]);
      graph[nr][nc] = cost + 1;
    }
  }
}

graph.forEach((e) => console.log(...e));
