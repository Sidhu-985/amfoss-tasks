n = 5

for i <- 1..n, rem(i, 2) == 1 do
  IO.puts String.duplicate(" ", div(n - i, 2)) <> String.duplicate("*", i)
end

for i <- (n-2)..1, rem(i, 2) == 1 do
  IO.puts String.duplicate(" ", div(n - i, 2)) <> String.duplicate("*", i)
end
