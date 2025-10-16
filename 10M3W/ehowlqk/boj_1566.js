const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1566.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((line) => line.split(" ").map(Number));

const [n, m] = input[0];
const A = input.slice(1);

const sign = (x) => (x > 0 ? 1 : x < 0 ? -1 : 0); // 부호 매핑

let best = n + m + 1; // 정답 도출

// 열 조합
for (let mask = 0; mask < 1 << m; mask++) {
  // -1 곱할 열 체크
  const c = Array(m);
  for (let j = 0; j < m; j++) c[j] = mask & (1 << j) ? -1 : 1;

  // -1 곱할 행 체크
  const r = Array(n);
  let ok = true;
  for (let i = 0; i < n; i++) {
    // 행의 합 구하기
    let s = 0;
    for (let j = 0; j < m; j++) s += A[i][j] * c[j];
    const sg = sign(s);

    // 행의 합이 0이라면 행 전체에 -1을 곱해도 0이므로 불가능
    if (sg === 0) {
      ok = false;
      break;
    }
    r[i] = sg;
  }
  if (!ok) continue;

  // 행의 부호 바꾼 후 열의 합 체크하기
  for (let j = 0; j < m && ok; j++) {
    let t = 0;
    for (let i = 0; i < n; i++) t += A[i][j] * r[i];
    const sg = sign(t);
    // 부호 바꾼 뒤에 열의 합 부호가 달라졌다면? -> 버린다
    if (sg !== c[j]) ok = false;
  }
  if (!ok) continue;

  // 부호 바꾼 횟수 count
  let flips = 0;
  for (let i = 0; i < n; i++) if (r[i] < 0) flips++;
  for (let j = 0; j < m; j++) if (c[j] < 0) flips++;
  if (flips < best) best = flips;
}

console.log(best === n + m + 1 ? -1 : best);
