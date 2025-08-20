const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M3W/ehowlqk/boj_12014.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (let tc = 0; tc < T; tc++) {
  const [n, k] = input[idx++].split(" ").map((e) => Number(e));
  const prices = input[idx++].split(" ").map((e) => Number(e));

  console.log("Case #" + Math.floor(idx / 2));
  console.log(LIS(prices, n, k));
}

function LIS(prices, n, k) {
  const lis = [prices[0]];
  for (let price of prices) {
    if (lis[lis.length - 1] < price) lis.push(price);
    else {
      let start = 0,
        end = lis.length - 1;

      while (start < end) {
        mid = Math.floor((start + end) / 2);
        if (lis[mid] < price) start = mid + 1;
        else end = mid;
      }

      lis[end] = price;
    }

    if (lis.length >= k) return 1;
  }
  return 0;
}
