function AC(p, arr) {
  let rev = false,
    delStart = 0,
    delEnd = 0;
  for (const cmd of p) {
    if (cmd === "R") {
      rev = !rev;
    } else {
      if (arr.length <= delStart + delEnd) {
        return "error";
      }
      if (rev) delEnd++;
      else delStart++;
    }
  }
  arrStr = rev
    ? String(arr.slice(delStart, arr.length - delEnd).reverse())
    : String(arr.slice(delStart, arr.length - delEnd));
  return "[" + arrStr + "]";
}

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M2W/ehowlqk/boj_5430.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

let idx = 0;
const T = Number(input[idx++]);
for (let tc = 0; tc < T; tc++) {
  const p = input[idx++];
  const n = Number(input[idx++]);
  let arr =
    input[idx++] === "[]"
      ? []
      : input[idx - 1].slice(1, input[idx - 1].length - 1).split(",");
  console.log(AC(p, arr));
}
