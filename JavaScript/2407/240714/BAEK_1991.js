const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let N;
let idx = 0;
const graph = Array.from({ length: 128}, () => []);

const dfsPreorder = (node, arr) => {
  if (node === 46) return;

  arr.push(String.fromCharCode(node));
  dfsPreorder(graph[node][0], arr);
  dfsPreorder(graph[node][1], arr);

  return arr;
}

const dfsInorder = (node, arr) => {
  if (node === 46) return;

  dfsInorder(graph[node][0], arr);
  arr.push(String.fromCharCode(node));
  dfsInorder(graph[node][1], arr);

  return arr;
}

const dfsPostorder = (node, arr) => {
  if (node === 46) return;

  dfsPostorder(graph[node][0], arr);
  dfsPostorder(graph[node][1], arr);
  arr.push(String.fromCharCode(node));

  return arr;
}

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else {
    let [a, b, c] = line.split(' ').map(String);
    // ASCII 코드로 변환 (0 ~ 127)
    a = a.charCodeAt(0);
    b = b.charCodeAt(0);
    c = c.charCodeAt(0);

    graph[a].push(b);
    graph[a].push(c);
  }

  idx++;
  if (idx === N+1) {
    rl.close();
  }
}).on('close', () => {
  const preorderResult = dfsPreorder(65, []);
  console.log(preorderResult.join(''));

  const inorderResult = dfsInorder(65, []);
  console.log(inorderResult.join(''));

  const postorderResult = dfsPostorder(65, []);
  console.log(postorderResult.join(''));
});