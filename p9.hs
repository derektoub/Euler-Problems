head [(a,b,c) | b <- [1..499], let a = (500000 - 1000*b) / (1000 - b), let c =sqrt (a^2 + b^2), a == fromInteger (round a)]
