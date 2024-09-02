const fs = require('fs');

function readFromFile(filename) {
  try {
    return parseInt(fs.readFileSync(filename, 'utf8').trim());
  } catch (err) {
    console.error('Error reading from file:', err);
    return null;
  }
}

function generateDiamond(n) {
  let diamond = '';

  for (let i = 1; i <= n; i += 2) {
    for (let j = 0; j < (n - i) / 2; j++) {
      diamond += ' ';
    }
  
    for (let k = 0; k < i; k++) {
      diamond += '*';
    }

    diamond += '\n';
  }

  for (let i = n - 2; i > 0; i -= 2) {
    for (let j = 0; j < (n - i) / 2; j++) {
      diamond += ' ';
    }

    for (let k = 0; k < i; k++) {
      diamond += '*';
    }

    diamond += '\n';
  }

  return diamond.trim();
}

function writeToFile(filename, content) {
  try {
    fs.writeFileSync(filename, content);
    console.log('Diamond pattern written to file:', filename);
  } catch (err) {
    console.error('Error writing to file:', err);
  }
}

const n = readFromFile('input.txt');

if (n !== null) {
  const diamondPattern = generateDiamond(n);

  writeToFile('output.txt', diamondPattern);
}
