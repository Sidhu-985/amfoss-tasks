use std::fs;

fn generate_diamond(n: usize) -> Vec<String> {
    let mut diamond = Vec::new();

    for i in (1..=n).step_by(2) {
        let spaces = " ".repeat((n - i) / 2);
        let stars = "*".repeat(i);
        diamond.push(format!("{}{}", spaces, stars));
    }

    for i in (1..n).rev().step_by(2) {
        let spaces = " ".repeat((n - i) / 2);
        let stars = "*".repeat(i);
        diamond.push(format!("{}{}", spaces, stars));
    }

    diamond
}

fn main() {
    let n: usize = fs::read_to_string("input.txt")
        .expect("Unable to read input.txt")
        .trim()
        .parse()
        .expect("Input is not a valid number");

    let diamond_pattern = generate_diamond(n);

    fs::write("output.txt", diamond_pattern.join("\n"))
        .expect("Unable to write to output.txt");

    println!("Diamond pattern written to output.txt");
}
