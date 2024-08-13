const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let F, S, G, U, D;

rl.on('line', (line) => {
  [F, S, G, U, D] = line.split(' ').map(Number);
}).on('close', () => {
  const visited = new Array(F+1).fill(-1);

  const queue = [S];
  visited[S] = 0;

  while (queue.length > 0) {
    const now = queue.shift();
    if (now === G) break;

    const nextUp = now + U;
    if (nextUp <= F && visited[nextUp] === -1) {
      queue.push(nextUp);
      visited[nextUp] = visited[now] + 1;
    }
    const nextDown = now - D;
    if (nextDown <= F && nextDown >= 1 && visited[nextDown] === -1) {
      queue.push(nextDown);
      visited[nextDown] = visited[now] + 1;
    }
  }

  console.log(visited[G] === -1 ? "use the stairs" : visited[G]);
});