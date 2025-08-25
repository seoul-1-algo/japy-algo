const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./8M3W/ehowlqk/boj_2239.txt";
const sudoku = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.split("").map((num) => Number(num)));

const usedRow = Array.from({ length: 9 }, () => []);
const usedCol = Array.from({ length: 9 }, () => []);
const usedBlock = Array.from({ length: 3 }, () =>
  Array.from({ length: 3 }, () => [])
);

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (sudoku[i][j]) {
      usedRow[i].push(sudoku[i][j]);
      usedCol[j].push(sudoku[i][j]);
      usedBlock[Math.floor(i / 3)][Math.floor(j / 3)].push(sudoku[i][j]);
    }
  }
}

function backtracking(row, col) {
  if (row === 9) {
    for (let line of sudoku) {
      console.log(line.join(""));
    }
    return true;
  }

  const next = col === 8 ? [row + 1, 0] : [row, col + 1];

  if (sudoku[row][col]) return backtracking(...next);
  const candidates = check(row, col);
  for (let candidate of candidates) {
    sudoku[row][col] = candidate;
    usedRow[row].push(candidate);
    usedCol[col].push(candidate);
    usedBlock[Math.floor(row / 3)][Math.floor(col / 3)].push(candidate);
    if (backtracking(...next)) return true;
    sudoku[row][col] = 0;
    usedRow[row].pop();
    usedCol[col].pop();
    usedBlock[Math.floor(row / 3)][Math.floor(col / 3)].pop();
  }
}

function check(row, col) {
  const nums = Array.from({ length: 9 }, (_, i) => i + 1);
  return nums.filter(
    (e) =>
      !usedRow[row].includes(e) &&
      !usedCol[col].includes(e) &&
      !usedBlock[Math.floor(row / 3)][Math.floor(col / 3)].includes(e)
  );
}

backtracking(0, 0);
