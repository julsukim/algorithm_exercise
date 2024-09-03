const input = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input_19583.txt')
  .toString()
  .trim()
  .split('\n')
  .map(line => line.trim());

const timeToMinutes = (timeStr) => {
  const [hours, minutes] = timeStr.split(':').map(Number);
  return hours * 60 + minutes;
}

const [S, E, Q] = input.shift().split(' ');

const startTime = timeToMinutes(S);
const endTime = timeToMinutes(E);
const quitTime = timeToMinutes(Q);

const entered = new Set();
const exited = new Set();

input.forEach(log => {
  const [timeStr, nickName] = log.split(' ');
  const time = timeToMinutes(timeStr);

  if (time <= startTime) {
    entered.add(nickName);
  } else if (time >= endTime && time <= quitTime) {
    exited.add(nickName);
  }
});

const confirmedAttendance = new Set([...entered].filter(nickName => exited.has(nickName)));
console.log(confirmedAttendance.size);