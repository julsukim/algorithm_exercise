// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let N;
	const heights = [];
	let idx = 0;
	
	const countBridge = (num, arr) => {
		let count = 0;
		const stack = [];
		
		for (let i = 0; i < num; i++) {
			while (stack.length > 0 && arr[i] >= arr[stack[stack.length - 1]]) {
				if (arr[i] === arr[stack.pop()]) {
					count++;
					break;
				}
			}
			stack.push(i);
		}
		
		return count;
	}
	
	for await (const line of rl) {
		if (idx === 0) {
			N = parseInt(line);
		} else {
			heights.push(...line.split(' ').map(Number));
		}
		idx++;
		if (idx === 2) {
			rl.close();
		}
	}
	
	const result = countBridge(N, heights);
	console.log(result);
	
	process.exit();
})();
