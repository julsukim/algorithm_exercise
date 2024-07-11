// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let N, L, R;
	const arts = [];
	let idx = 0;
	
	const countArts = (N, L, R, arts) => {
		const prefixSum = new Array(N + 1).fill(0);
		
		for (let i = 1; i <= N; i++) {
			prefixSum[i] = prefixSum[i - 1] + arts[i - 1];
		}
		
		let count = 0;
		
		for (let a = 1; a <= N; a++) {
			for (let b = a; b <= N; b++) {
				let totalPrice = prefixSum[b] - prefixSum[a - 1];
				if (totalPrice >= L && totalPrice <= R) {
					count++;
				}
			}
		}
		
		return count;
	}
	
	for await (const line of rl) {
		if (idx === 0) {
			[N, L, R] = line.split(' ').map(Number);
		} else {
			arts.push(...line.split(' ').map(Number));
		}
		idx++;
		if (idx == 2) {
			rl.close();
		}
	}
	
	const result = countArts(N, L, R, arts);
	console.log(result);
	
	process.exit();
})();
