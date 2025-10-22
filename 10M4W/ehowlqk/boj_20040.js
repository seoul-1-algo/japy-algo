const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_20040.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(input) {
  // find 함수
  function find(x) {
    if (parents[x] !== x) {
      parents[x] = find(parents[x]);
    }
    return parents[x];
  }

  // union 함수
  function union(x, y) {
    const [rootX, rootY] = [find(x), find(y)];
    if (rootX > rootY) {
      parents[rootX] = rootY;
    } else parents[rootY] = rootX;
  }

  const [n, m] = input[0].split(" ").map((e) => Number(e));
  const parents = Array.from({ length: n }, (_, idx) => idx);

  for (let i = 1; i < m + 1; ++i) {
    const [a, b] = input[i].split(" ").map((e) => Number(e));
    if (find(a) === find(b)) return i; // 사이클 완성 시 인덱스 반환
    union(a, b);
  }

  return 0; // m번 진행 후 종료 X => 0 반환
}

console.log(solution(input));
