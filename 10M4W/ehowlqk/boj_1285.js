const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1285.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/** row별로 비트화하기 */
function toBitRows(matrix, n) {
  const rows = new Array(n);

  for (let r = 0; r < n; r++) {
    let bits = 0;
    const line = matrix[r];
    for (let c = 0; c < n; c++) {
      if (line[c] === "T") bits = bits | (1 << c); // T(뒷면) 위치를 1로 하여 비트로 저장
    }
    rows[r] = bits;
  }

  return rows;
}

/** x비트 내 1의 개수 세기(Kernighan's algorithm) */
function popcount(x) {
  let cnt = 0;
  while (x) {
    x &= x - 1;
    cnt++;
  }
  return cnt;
}

function solution(input) {
  const [n, ...coins] = input;
  const N = Number(n);
  let answer = Number.MAX_SAFE_INTEGER;

  const coinBits = toBitRows(coins, N);
  for (let colMask = 0; colMask < 1 << N; colMask++) {
    let sum = 0;
    for (let r = 0; r < N; r++) {
      const flipped = coinBits[r] ^ colMask; // XOR 연산 -> colMask로 뒤집은 결과
      const tails = popcount(flipped);
      sum += Math.min(tails, N - tails); // row 뒤집기로 최소값 더하기
      if (sum > answer) break; // 가지치기
    }
    if (answer > sum) answer = sum;
  }
  return answer;
}

console.log(solution(input));
