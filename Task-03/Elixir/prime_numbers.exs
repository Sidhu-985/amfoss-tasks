# prime_numbers_script.exs

IO.write("Enter a value for n: ")
n = String.trim(IO.readln()) |> String.to_integer()

if n <= 1 do
  IO.puts("#{n} is not a prime number")
else
  for i <- 2..n do
    flag = Enum.any?(2..trunc(:math.sqrt(i)), fn j -> rem(i, j) == 0 end)
    if not flag do
      IO.puts("#{i} is a prime number")
    end
  end
end

# Use elixir prime_numbers_script.exs command to run the file in terminal.
