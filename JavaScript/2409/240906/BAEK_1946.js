const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_1946.txt')
  .toString()
  .trim()
  .split('\n');

let idx = 0;
const TC = parseInt(input[idx++]);
const result = [];

for (let t = 0; t < TC; t++) {
  const N = parseInt(input[idx++]);  // 지원자 수
  const candidates = [];

  for (let i = 0; i < N; i++) {
    candidates.push(input[idx++].split(' ').map(Number));
  }

  // 서류 성적을 기준으로 오름차순 정렬
  candidates.sort((a, b) => a[0] - b[0]);

  let count = 1;  // 첫 번째 사람은 무조건 선발
  let minInterviewRank = candidates[0][1];  // 첫 번째 사람의 면접 성적

  // 서류 성적 1등부터 시작해서 비교
  for (let i = 1; i < N; i++) {
    if (candidates[i][1] < minInterviewRank) {
      count++;
      minInterviewRank = candidates[i][1];  // 새로운 최소 면접 성적 업데이트
    }
  }

  result.push(count);
}

console.log(result.join('\n'));