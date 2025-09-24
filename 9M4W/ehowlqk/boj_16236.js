const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_16236.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let idx = 0;
const n = Number(input[idx++]);
const space = [];
let visited = Array.from({ length: n }, () =>
  Array.from({ length: n }, () => false)
);

let queue = [];

for (idx; idx < n + 1; idx++) {
  const line = input[idx].split(" ").map((num) => Number(num));
  const sharkCol = line.indexOf(9); // 상어 위치 찾기
  if (sharkCol >= 0) {
    queue.push([idx - 1, sharkCol]);
    line[sharkCol] = 0;
    visited[idx - 1][sharkCol] = true;
  }
  space.push(line);
}

let sharkSize = 2,
  feedCount = 0,
  time = 0; // 아기상어의 크기, 먹은 물고기 수, 걸리는 시간

// 가까운 애들 중 위쪽, 왼쪽 순으로 우선순위 적용
const dr = [-1, 0, 0, 1],
  dc = [0, -1, 1, 0];

let findD = 0,
  findR = n,
  findC = n,
  found = false;


while (queue.length) {
  const tmp = [];
  // 같은 거리에 있는 모든 노드 탐색
  for (const [row, col] of queue) {
    // 먹을 수 있는 물고기가 있는 경우
    if (
      0 < space[row][col] &&
      space[row][col] < sharkSize &&
      (row < findR || (row === findR && col < findC))
    ) {
      found = true;
      findR = row;
      findC = col;
    }

    // 아직 먹을 수 있는 물고기 찾지 못한 경우
    if (!found) {
      for (let i = 0; i < 4; i++) {
        const nr = row + dr[i],
          nc = col + dc[i];
        if (
          0 <= nr &&
          nr < n &&
          0 <= nc &&
          nc < n &&
          space[nr][nc] <= sharkSize &&
          !visited[nr][nc]
        ) {
          tmp.push([nr, nc]);
          visited[nr][nc] = true;
        }
      }
    }
  }

  // 먹을 수 있는 물고기를 찾은 경우
  if (found) {
    feedCount++; // 먹은 물고기 수 추가
    space[findR][findC] = 0; // 먹은 칸 0 처리
    // 내 크기만큼 먹었을 경우 크기 1 증가,  먹은 물고기 수 초기화
    if (feedCount >= sharkSize) {
      sharkSize++;
      feedCount = 0;
    }
    time += findD; // 총 걸린 시간 추가
    findD = 0; // 시간 초기화
    // 방문배열 초기화
    visited = Array.from({ length: n }, () =>
      Array.from({ length: n }, () => false)
    );
    visited[findR][findC] = true;
    // 큐 초기화
    queue = [];
    for (let i = 0; i < 4; i++) {
      const nr = findR + dr[i],
        nc = findC + dc[i];
      if (
        0 <= nr &&
        nr < n &&
        0 <= nc &&
        nc < n &&
        space[nr][nc] <= sharkSize &&
        !visited[nr][nc]
      ) {
        queue.push([nr, nc, findD + 1]);
        visited[nr][nc] = true;
      }
    }
    findR = n;
    findC = n;
    found = false;
  } else {
    queue = [...tmp];
    findD++;
  }
}

console.log(time);
