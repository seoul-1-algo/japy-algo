const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./1074.txt";

const input = fs.readFileSync(filePath).toString().trim().split(" ");

const [N, R, C] = input.map(Number);

function Z(n, r, c) {
  if (n === 0) {
    return 0;
  }

  const half = 2 ** (n - 1)
  const size = half * half

  if (r < half && c < half) {
    return Z(n - 1, r, c)
  } else if (r < half && c >= half) {
    return size + Z(n - 1, r, c - half)
  } else if (r >= half && c < half) {
    return 2 * size + Z(n - 1, r - half, c)
  } else {
    return 3 * size + Z(n - 1, r - half, c - half)
  }
}

console.log(Z(N, R, C))