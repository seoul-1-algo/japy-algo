const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_11054.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function bitonic(n, arr) {
  const lis = LIS(n, arr);
  const lds = LDS(n, arr);

  let answer = 0;
  for (let i = 0; i < n; ++i) {
    answer = Math.max(answer, lis[i] + lds[i] - 1);
  }

  return answer
}

/** i에서 끝나는 LIS: arr[i] 작은 수 까지의 LIS 최대 길이 + 1 */
function LIS(n, arr) {
  const result = Array(n).fill(1);

  for (let i = 0; i < n; ++i) {
    for (let j = 0; j < i; ++j) {
      if (arr[i] > arr[j]) {
        result[i] = Math.max(result[i], result[j] + 1);
      }
    }
  }

  return result;
}

function LDS(n, arr) {
  const result = Array(n).fill(1);
  // i에서 끝나는 LIS: arr[i] 작은 수 까지의 LIS 최대 길이 + 1
  for (let i = n - 1; i >= 0; --i) {
    for (let j = n - 1; j >= i; --j) {
      if (arr[i] > arr[j]) {
        result[i] = Math.max(result[i], result[j] + 1);
      }
    }
  }

  return result;
}

const n = Number(input[0]);
const arr = input[1].split(" ").map((e) => Number(e));
console.log(bitonic(n, arr));
