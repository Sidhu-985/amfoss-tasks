const n = 5;  

for (let i = 1; i <= n; i += 2) {  
    let line = '';
    for (let j = 0; j < (n - i) / 2; j++) {
        line += ' ';
    }

    for (let k = 0; k < i; k++) {
        line += '*';
    }

    console.log(line);
}

for (let i = n - 2; i > 0; i -= 2) { 
    let line = '';
    for (let j = 0; j < (n - i) / 2; j++) {
        line += ' ';
    }

    for (let k = 0; k < i; k++) {
        line += '*';
    }

    console.log(line);
}
