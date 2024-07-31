let iterations = 0;
const start = performance.now();

while (performance.now() - start < 1000) {
  iterations++;
}

console.log(`${iterations} per seconds`);