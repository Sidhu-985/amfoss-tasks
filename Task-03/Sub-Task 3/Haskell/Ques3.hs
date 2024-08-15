n = 5

main = do
    mapM_ putStrLn [replicate ((n - i) `div` 2) ' ' ++ replicate i '*' | i <- [1,3..n]]

    mapM_ putStrLn [replicate ((n - i) `div` 2) ' ' ++ replicate i '*' | i <- [n-2,n-4..1]]
