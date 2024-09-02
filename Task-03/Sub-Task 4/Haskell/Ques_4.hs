import Data.List (intercalate)

generateDiamond :: Int -> [String]
generateDiamond n = topHalf ++ bottomHalf
  where
    topHalf = [replicate (n - i) ' ' ++ replicate (2 * i - 1) '*' | i <- [1..n]]
    bottomHalf = reverse $ drop 1 topHalf

main :: IO ()
main = do
  n <- read <$> readFile "input.txt"
  writeFile "output.txt" $ unlines $ generateDiamond n
  putStrLn "Diamond pattern written to output.txt"
