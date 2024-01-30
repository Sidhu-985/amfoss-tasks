function prime_numbers(n) {
  if (n <= 1) {
    console.log(n + " is not a prime number");
  } else {
    for (let i = 2; i <= n; i++) {
      let flag = 0;
      for (let j = 2; j <= Math.sqrt(i); j++) {
        if (i % j === 0) {
          flag = 1;
          break; 
        }
      }
      if (flag === 0) {
        console.log(i + " is a prime number");
      }
    }
  }
}

let num = prompt("Enter a value for n: ");
let n = parseInt(num);

prime_numbers(n);
