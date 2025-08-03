const fs = require("fs");
const input = fs
  .readFileSync("./8M1W/ehowlqk/boj_7569.txt")
  .toString()
  .trim()
  .split("\n");

let idx = 0;

const [M, N, H] = input[idx++].split(" ").map((e) => Number(e));

const boxes = [];
for (idx; idx < N * H + 1; idx += N) {
  const box = [];
  for (let i = idx; i < idx + N; i++) {
    box.push(input[i].split(" ").map((e) => Number(e)));
  }
  boxes.push(box);
}

const dm = [1, -1, 0, 0, 0, 0],
  dn = [0, 0, 1, -1, 0, 0],
  dh = [0, 0, 0, 0, 1, -1];

function bfs(boxes) {
  // 큐에 익은 토마토 위치 모두 추가
  const q = [];
  let head = 0;
  for (let h = 0; h < H; h++) {
    for (let n = 0; n < N; n++) {
      for (let m = 0; m < M; m++) {
        if (boxes[h][n][m] === 1) q.push([m, n, h, 0]);
      }
    }
  }

  let days = 0; // 최대 시간 초기화
  // bfs 진행
  while (head < q.length) {
    const [x, y, z, time] = q[head++];
    days = Math.max(days, time);
    for (let i = 0; i < 6; i++) {
      const nx = x + dm[i],
        ny = y + dn[i],
        nz = z + dh[i];
      if (
        0 <= nx &&
        nx < M &&
        0 <= ny &&
        ny < N &&
        0 <= nz &&
        nz < H &&
        !boxes[nz][ny][nx]
      ) {
        q.push([nx, ny, nz, time + 1]);
        boxes[nz][ny][nx] = 1;
      }
    }
  }

  // 안 익은 토마토 있는지 확인
  for (let h = 0; h < H; h++) {
    for (let n = 0; n < N; n++) {
      for (let m = 0; m < M; m++) {
        if (boxes[h][n][m] === 0) return -1;
      }
    }
  }

  return days;
}

console.log(bfs(boxes));
