print "Enter a value for n: "
n = gets.chomp.to_i

if n <= 1
  puts "#{n} is not a prime number"
else
  (2..n).each do |i|
    flag = 0
    (2..Math.sqrt(i).to_i).each do |j|
      if (i % j).zero?
        flag = 1
        break
      end
    end
    puts "#{i} is a prime number" if flag.zero?
  end
end
