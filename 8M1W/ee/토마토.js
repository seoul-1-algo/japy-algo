const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./7569.txt";

const input = fs.readFileSync(filePath).toString().trim().split('\n');

// 상자 크기 정보
const [M, N, H] = input[0].split(' ').map(Number);

// 토마토 정보 3차원 배열로 저장
let idx = 1;
const tomatoes = [];

for (let h = 0; h < H; h++) {
  const temp = [];
  for (let n = 0; n < N; n++) {
    temp.push(input[idx++].split(' ').map(Number));
  }
  tomatoes.push(temp);
}

let days = 0; // 모든 토마토가 익을 때까지 며칠이 걸리는 지
let cnt = 0;  // 익은 토마토의 수

let q = [];  // 하지만 자바스크립트에는 큐가 없다
let head = 0;

for (let i = 0; i < H; i++) {
  for (let j = 0; j < N; j++) {
    for (let k = 0; k < M; k++) {
      if (tomatoes[i][j][k] === 0) {
        continue;
      }

      if (tomatoes[i][j][k] === 1) {
        q.push([i, j, k]);
      }

      cnt += 1;
    }
  }
}

if (cnt === M * N * H) {
  console.log(0);
  process.exit(); // 자스에서 탈출하는 법 !!!!!!!!!!
}

// BFS

const di = [1, -1, 0, 0, 0, 0];
const dj = [0, 0, 1, -1, 0, 0];
const dk = [0, 0, 0, 0, 1, -1];

while (head < q.length) {
  const [i, j, k] = q[head++];

  for (let l = 0; l < 6; l++) {
    const ni = i + di[l];
    const nj = j + dj[l];
    const nk = k + dk[l];

    if (0 <= ni && ni < H && 0 <= nj && nj < N && 0 <= nk && nk < M && tomatoes[ni][nj][nk] === 0) {
      tomatoes[ni][nj][nk] = tomatoes[i][j][k] + 1;
      q.push([ni, nj, nk]);

      cnt++;
      days = Math.max(days, tomatoes[ni][nj][nk]);
    }
  }
}

console.log(cnt < M * N * H ? -1 : days - 1);
