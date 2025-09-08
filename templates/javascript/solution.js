const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
function solve(input) {
    const lines = input.trim().split('\n');
    return result;
}

let input = '';
rl.on('line', (line) => {
    input += line + '\n';
});

rl.on('close', () => {
    const result = solve(input);
    console.log(result);
});