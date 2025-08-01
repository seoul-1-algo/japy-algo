const fs = require("fs");
const [N, r, c] = fs
  .readFileSync("./7M4W/ehowlqk/boj_1074.txt")
  .toString()
  .split(" ")
  .map((e) => Number(e));

function z(size, row, col) {
  const loc = zone(2 ** size, row, col);
  if (size === 1) {
    return loc - 1;
  }
  let order = 0;
  const div = 2 ** (size - 1);
  const add = (2 ** size) ** 2 / 4;
  switch (loc) {
    case 4:
      order += add;
    case 3:
      order += add;
    case 2:
      order += add;
    default:
      break;
  }

  return order + z(size - 1, row % div, col % div);
}

function zone(size, row, col) {
  if (row < size / 2) {
    if (col < size / 2) {
      return 1;
    } else return 2;
  } else {
    if (col < size / 2) {
      return 3;
    } else return 4;
  }
}

console.log(z(N, r, c));
