const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

rl.on('line', (line) => {
    const tc = line
    if (tc === '0') {
        rl.close()
    } else {
        const result = isPalindrome(tc)
        if (result) {
            console.log("yes")
        } else {
            console.log("no")
        }
    }
})

const isPalindrome = (str) => {
    let len = str.length

    for (let i = 0; i < len / 2; i++) {
        if (str[i] !== str[len -1 -i]) {
            return false
        }
    }
    return true
}
