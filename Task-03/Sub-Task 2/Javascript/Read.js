const fs = require('fs');

const content = fs.readFileSync('input.txt', 'utf8');
fs.writeFileSync('output.txt', content);
