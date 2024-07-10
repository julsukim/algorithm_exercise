const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N;
const arr = [];
let idx = 0;

rl.on('line', (line) => {
  if (idx === 0) {
    N = parseInt(line);
  } else {
    arr.push(line.split(' ').map(Number));
  }
  idx++;
  if (idx === N+1) {
    rl.close();
  }
}).on('close', () => {

  let result = 1;
  const maxHeight = Math.max(...arr.flat());
  const delta = [[-1, 0], [0, 1], [1, 0], [0, -1]];

  for (let h=0; h<=maxHeight; h++) {

    let count = 0;
    const sink = new Array(N).fill(false).map(() => new Array(N).fill(false));

    for (let i=0; i<N; i++) {
      for (let j=0; j<N; j++) {
        if (arr[i][j] > h && !sink[i][j]) {
          count += 1;
          sink[i][j] = true;
          const queue = [];
          queue.push([i, j]);

          while (queue.length > 0) {
            const [pi, pj] = queue.shift();

            for (const [di, dj] of delta) {
              const ni = pi + di;
              const nj = pj + dj;

              if (0<=ni && ni<N && 0<=nj && nj<N) {
                if (!sink[ni][nj] && arr[ni][nj] > h) {
                  sink[ni][nj] = true;
                  queue.push([ni, nj]);
                }
              }
            }
          }
        }
      }
    }
    result = Math.max(result, count);
  }

  console.log(result);
});