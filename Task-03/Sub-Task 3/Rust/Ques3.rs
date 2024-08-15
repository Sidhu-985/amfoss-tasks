fn main() {
    let n = 5;

    for i in (1..=n).step_by(2) {
        println!(
            "{}{}",
            " ".repeat((n - i) / 2),
            "*".repeat(i)
        );
    }

    for i in (1..n).rev().step_by(2) {
        println!(
            "{}{}",
            " ".repeat((n - i) / 2),
            "*".repeat(i)
        );
    }
}
