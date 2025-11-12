const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1167.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let idx = 0;
const v = Number(input[idx++]);

const edges = Array.from({ length: v + 1 }, () => []);

// 간선처리
for (idx; idx < input.length; idx++) {
  const tmp = input[idx].split(" ").map((e) => Number(e));

  let node = 1;
  while (tmp[node] > 0) {
    edges[tmp[0]].push([tmp[node], tmp[node + 1]]);
    node += 2;
  }
}

// start로부터 가장 먼 노드와 거리 찾기
function findFurthest(start, edges, v) {
  visited = Array(v + 1).fill(false);
  visited[start] = true;
  const stack = [[start, 0]];

  let maxDist = 0,
    furthest = start;

  while (stack.length) {
    const [node, cost] = stack.pop();

    if (cost > maxDist) {
      maxDist = cost;
      furthest = node;
    }

    for (const [nxt, dist] of edges[node]) {
      if (!visited[nxt]) {
        stack.push([nxt, cost + dist]);
        visited[nxt] = true;
      }
    }
  }

  return [maxDist, furthest];
}

const EoD = findFurthest(1, edges, v)[1];
console.log(findFurthest(EoD, edges, v)[0]);
