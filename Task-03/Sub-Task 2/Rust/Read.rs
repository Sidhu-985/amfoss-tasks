use std::fs;

fn main() {
    let content = fs::read_to_string("input.txt");
    fs::write("output.txt", content).expect("Failed to write file");
}
