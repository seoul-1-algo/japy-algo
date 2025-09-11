const fs = require('fs');

const START = [0, 0];
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

function backTracking(curX, curY, depth) {
    const remainingAlphabets = 26 - visited.reduce((sum, v) => sum + (v ? 1 : 0), 0);
    if (depth + remainingAlphabets <= answer) {
        return;
    }
    
    if (depth > answer) {
        answer = depth;
    }
    if (answer === 26) {
        return;
    }

    for (let k = 0; k < 4; k++) {
        const nx = curX + dx[k];
        const ny = curY + dy[k];
        if (0 <= nx && nx < R && 0 <= ny && ny < C) {
            const alphaIdx = board[nx][ny].charCodeAt(0) - 'A'.charCodeAt(0);
            if (!visited[alphaIdx]) {
                visited[alphaIdx] = true;
                backTracking(nx, ny, depth + 1);
                visited[alphaIdx] = false;
            }
        }
    }
}

const data = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const [R, C] = data[0].split(' ').map(Number);
const board = data.slice(1).map(line => line.trim());

let answer = 0;
let visited = new Array(26).fill(false);
visited[board[0][0].charCodeAt(0) - 'A'.charCodeAt(0)] = true;
backTracking(START[0], START[1], 1);

console.log(answer);
