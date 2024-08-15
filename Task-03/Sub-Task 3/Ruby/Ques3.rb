n = 5

(1..n).step(2) do |i|
  puts ' ' * ((n - i) / 2) + '*' * i
end

(n-2).step(1, -2) do |i|
  puts ' ' * ((n - i) / 2) + '*' * i
end
