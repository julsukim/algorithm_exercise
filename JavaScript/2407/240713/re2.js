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
        const prefixSums = new Map();
        prefixSums.set(0, 1); // prefixSum of 0 has one occurrence
        
        for (let b = 1; b <= N; b++) {
            let totalPrice = prefixSum[b];
            
            // Check for sums within [L, R]
            let minSum = totalPrice - R;
            let maxSum = totalPrice - L;

            for (let [sum, occurrences] of prefixSums.entries()) {
                if (sum >= minSum && sum <= maxSum) {
                    count += occurrences;
                }
            }
            
            // Update the prefixSums map
            if (prefixSums.has(totalPrice)) {
                prefixSums.set(totalPrice, prefixSums.get(totalPrice) + 1);
            } else {
                prefixSums.set(totalPrice, 1);
            }
        }
        
        return count;
    };
    
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
