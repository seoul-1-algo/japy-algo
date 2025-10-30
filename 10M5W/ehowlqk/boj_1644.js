const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "boj_1644.txt";
const input = fs.readFileSync(filePath).toString();

const N = Number(input);

const primes = Array(N + 1).fill(true);
(primes[0] = false), (primes[1] = false);

const sums = [0];

// 누적합 배열
for (let i = 1; i <= N; i++) {
  if (primes[i]) {
    for (let j = i; j <= N; j += i) {
      if (j === i) continue;
      primes[j] = false;
    }
    sums.push(sums[sums.length - 1] + i);
  }
}

let answer = 0,
  start = 0,
  end = 0;

while (start <= end && end < sums.length) {
  const cur_sum = sums[end] - sums[start];
  if (cur_sum < N) {
    end++;
  } else if (cur_sum > N) {
    start++;
  } else {
    answer++;
    end++;
    start++;
  }
}

console.log(answer);

function isPrime(num) {
  if (num === 1) return false;
  for (let k = 2; k < num; k++) {
    if (num % k === 0) return false;
  }
  return true;
}
