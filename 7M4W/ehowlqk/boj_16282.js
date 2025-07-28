const fs = require("fs");
const n = BigInt(fs.readFileSync("./7M4W/ehowlqk/boj_16282.txt").toString());

// n개의 고리를 만들 경우
// n g까지는 만들 수 있음
// 따라서 끊은 애들 사이에 (n+1)g 만큼의 덩어리가 필요하다
// 그 다음엔 (n+1 + n)g까지는 만들 수 있음
// 따라서 그 다음 틈에 (n+1 + n + 1)g이 필요하다
// ...(n+1번 반복)
// 이걸 식으로 풀어내면 위와 같은 식이 나온다.

const base = 2n;
let power = 1n;
while (n > (power + 1n) * base ** (power + 1n) - 1n) power++;

console.log(Number(power));
