use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter a value for n: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");

    let n: usize = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a valid number.");
            return;
        }
    };

    if n <= 1 {
        println!("{} is not a prime number", n);
    } else {
        for i in 2..=n {
            let mut flag = 0;
            for j in 2..=(i as f64).sqrt() as usize {
                if i % j == 0 {
                    flag = 1;
                    break;
                }
            }
            if flag == 0 {
                println!("{} is a prime number", i);
            }
        }
    }
}
