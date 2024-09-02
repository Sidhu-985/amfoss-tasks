def generate_diamond(n)
  diamond = []

  (1..n).step(2) do |i|
    spaces = ' ' * ((n - i) / 2)
    stars = '*' * i
    diamond << spaces + stars
  end

  (n - 2).step(1, -2) do |i|
    spaces = ' ' * ((n - i) / 2)
    stars = '*' * i
    diamond << spaces + stars
  end

  diamond
end

n = File.read('input.txt').to_i

diamond_pattern = generate_diamond(n)

File.open('output.txt', 'w') do |file|
  file.puts diamond_pattern
end

puts "Diamond pattern written to output.txt"
