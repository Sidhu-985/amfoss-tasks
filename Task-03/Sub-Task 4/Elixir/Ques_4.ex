defmodule DiamondPattern do
  def generate_diamond(n, output_file) do
    for i <- 1..n//2 do
      leading_spaces = String.duplicate(" ", n - 2 * i + 1)
      asterisks = String.duplicate("*", 2 * i - 1)
      IO.puts(output_file, leading_spaces <> asterisks)
    end

    for i <- (n//2-1)..0 do
      leading_spaces = String.duplicate(" ", n - 2 * i + 1)
      asterisks = String.duplicate("*", 2 * i - 1)
      IO.puts(output_file, leading_spaces <> asterisks)
    end
  end
end

defmodule Main do
  def main do
    n = read_from_file("input.txt")
    {:ok, output_file} = File.open("output.txt", [:write])
    DiamondPattern.generate_diamond(n, output_file)
    File.close(output_file)
    IO.puts("Diamond pattern written to output.txt")
  end

  defp read_from_file(filename) do
    case File.read(filename) do
      {:ok, contents} ->
        String.trim(contents) |> String.to_integer()

      {:error, reason} ->
        IO.puts("Error reading from #{filename}: #{reason}")
        exit(:normal)
    end
  end
end

Main.main()
