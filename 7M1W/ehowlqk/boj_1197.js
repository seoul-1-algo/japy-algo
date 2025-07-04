class Prim {
  constructor(nodes, edges) {
    this.nodes = nodes;
    this.edges = edges;
    this.visited = Array(Number(nodes) + 1).fill(false);
    this.queue = [];
  }

  size() {
    return this.queue.length;
  }

  left(index) {
    return (index + 1) * 2 - 1;
  }

  right(index) {
    return (index + 1) * 2;
  }

  parent(index) {
    return Math.floor((index + 1) / 2) - 1;
  }

  child(index) {
    let right = this.right(index),
      left = this.left(index);
    if (right < this.size() && this.queue[right][0] < this.queue[left][0]) {
      return right;
    }
    return left;
  }

  swap(idx1, idx2) {
    [this.queue[idx1], this.queue[idx2]] = [this.queue[idx2], this.queue[idx1]];
  }

  enqueue(elem) {
    this.queue.push(elem);
    const size = this.size();
    let idx = size - 1,
      parent = this.parent(idx);
    while (idx > 0) {
      if (this.queue[parent][0] > this.queue[idx][0]) {
        this.swap(idx, parent);
        idx = parent;
        parent = this.parent(parent);
      } else {
        return;
      }
    }
  }

  dequeue() {
    this.swap(0, this.size() - 1);
    const result = this.queue.pop();
    let idx = 0;
    while (this.left(idx) < this.size()) {
      let child = this.child(idx);
      if (this.queue[child][0] < this.queue[idx][0]) {
        this.swap(child, idx);
        idx = child;
      } else {
        break;
      }
    }
    return result;
  }

  answer() {
    this.enqueue([0, 1]);
    let totalCost = 0;
    while (this.size() > 0) {
      const [cost, curr] = this.dequeue();
      if (this.visited[curr] === true) {
        continue;
      }
      this.visited[curr] = true;
      totalCost += cost;
      this.edges[curr].forEach(([dist, node]) => {
        if (!this.visited[node]) {
          this.enqueue([dist, node]);
        }
      });
    }
    return totalCost;
  }
}

const fs = require("fs");
const input = fs
  .readFileSync("./7M1W/ehowlqk/boj_1197.txt")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.trim("/r"));

let idx = 0;
const [v, e] = input[idx++].split(" ");

const edges = Array.from({ length: Number(v) + 1 }, () => new Array());

for (idx; idx < input.length; idx++) {
  const [a, b, c] = input[idx].split(" ").map((e) => Number(e));
  edges[a].push([c, b]);
  edges[b].push([c, a]);
}

const mst = new Prim(v, edges);
console.log(mst.answer());
