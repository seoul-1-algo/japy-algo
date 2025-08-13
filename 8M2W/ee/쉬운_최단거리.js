const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./14940.txt";

const input = fs.readFileSync(filePath).toString().trim().split('\n');

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

function bfs(i, j) {
  let queue = [];
  queue.push([i, j]);

  const visited = Array.from({length: n}, () => Array(m).fill(0));

  let front = 0;

  while (front < queue.length) {
    const [r, c] = queue[front++];
    
    for (let k = 0; k < 4; k++) {
      const nr = r + dr[k];
      const nc = c + dc[k];

      // 지도 범위 안에 있고, 방문하지 않았고, 갈 수 있는 땅이라면 
      if (0 <= nr && nr < n && 0 <= nc && nc < m && !visited[nr][nc] && arr[nr][nc] === 1) {
        queue.push([nr, nc]);
        visited[nr][nc] = visited[r][c] + 1;
      }
    }
  }

  return visited;
}

const [n, m] = input[0].split(' ').map(Number); // 지도의 크기
const arr = []; // 지도 정보를 저장할 배열 
for (let i = 1; i <= n; i++) {
  arr.push(input[i].split(' ').map(Number));
}

let answer = [] // 정답을 저장할 배열

// 목표 지점(2)에서 각 지점(1)까지의 거리 계산
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (arr[i][j] === 2) {
      answer = bfs(i, j);
    }
  }
}

// 원래 갈 수 있는 땅인데 도달할 수 없었다면 -1
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (answer[i][j] === 0 && arr[i][j] !== 0 && arr[i][j] !== 2) {
      answer[i][j] = -1;
    }
  }
}

// 정답 출력
for (let i = 0; i < n; i++) {
  console.log(answer[i].join(' '));
}