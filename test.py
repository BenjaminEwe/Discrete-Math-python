from discrete import *

#gcd tests
if not gcd(48, 18) == 6:
    print("Error in gcd function for inputs 48 and 18")
if not gcd(101, 10) == 1:
    print("Error in gcd function for inputs 101 and 10")
if not gcd(270270, 18) == 18:
    print("Error in gcd function for inputs 270270 and 18")
if not gcd(705705, 18) == 3:
    print("Error in gcd function for inputs 705705 and 18")

#gcd_bezout tests
if not gcd_bezout(48, 18) == (6, -1, 3):
    print("Error in gcd_bezout function for inputs 48 and 18")
if not gcd_bezout(101, 10) == (1, 1, -10):
    print("Error in gcd_bezout function for inputs 101 and 10")
if not gcd_bezout(270270, 18) == (18, 0, 1):
    print("Error in gcd_bezout function for inputs 270270 and 18")
if not gcd_bezout(705705, 18) == (3, -1, 39206):
    print("Error in gcd_bezout function for inputs 705705 and 18")

# isCoprime tests
if isCoprime(48, 18) != False:
    print("Error in isCoprime function for inputs 48 and 18")
if isCoprime(101, 10) != True:
    print("Error in isCoprime function for inputs 101 and 10")

# n-graph properties tests
if not graphProperties(5, 'complete') == {'vertices': 5, 'edges': 10, 'degree': [4, 4, 4, 4, 4]}:
    print("Error in graphProperties function for complete graph with 5 vertices")
if not graphProperties(4, 'cube') == {'vertices': 16, 'edges': 32, 'degree': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]}:
    print("Error in graphProperties function for cube graph with 4 dimensions")
if not graphProperties(6, 'cycle') == {'vertices': 6, 'edges': 6, 'degree': [2, 2, 2, 2, 2, 2]}:
    print("Error in graphProperties function for cycle graph with 6 vertices")
if not graphProperties(7, 'wheel') == {'vertices': 7, 'edges': 12, 'degree': [6, 3, 3, 3, 3, 3, 3]}:
    print("Error in graphProperties function for wheel graph with 7 vertices")

# Edge case tests
if not graphProperties(2, 'cycle') == {'error': 'A cycle graph must have at least 3 vertices'}:
    print("Error in graphProperties function for cycle graph with 2 vertices")
if not graphProperties(3, 'wheel') == {'error': 'A wheel graph must have at least 4 vertices'}:
    print("Error in graphProperties function for wheel graph with 3 vertices")

# Inclusion-Exclusion tests
if not inclusion_exclusion(3, 100, [30, 20]) == 230:
    print("Error in inclusion_exclusion function for inputs 100, [30, 20]")
if not inclusion_exclusion(4, 200, [50, 25, 5]) == 595:
    print("Error in inclusion_exclusion function for inputs 200, [50, 25, 5]")

# Choose tests
if not choose(5, 2) == 10:
    print("Error in choose function for inputs 5 and 2")
if not choose(10, 5) == 252:
    print("Error in choose function for inputs 10 and 5")

if not binom(5, 2) == 10:
    print("Error in binom function for inputs 5 and 2")
if not binom(10, 5) == 252:
    print("Error in binom function for inputs 10 and 5")

# Derangement tests
if not derange(4) == 9:
    print("Error in derangement function for input 4")
if not derange(5) == 44:
    print("Error in derangement function for input 5")
if not derange(0) == 1:
    print("Error in derangement function for input 0")
if not derange(-45) == -1:
    print("Error in derangement function for input -45")
if not derange(29) == 3252702461227859257745914274516:
    print("Error in derangement function for input 29")
    

# Primes under tests
if not primesUnder(10) == [2, 3, 5, 7]:
    print("Error in primesUnder function for input 10")
if not primesUnder(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
    print("Error in primesUnder function for input 30")
if not primesUnder(1) == []:
    print("Error in primesUnder function for input 1")
if not primesUnder(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]:
    print("Error in primesUnder function for input 50")

# isPrime tests
if not isPrime(29) == True:
    print("Error in isPrime function for input 29")
if not isPrime(100) == False:
    print("Error in isPrime function for input 100")
if not isPrime(1) == False:
    print("Error in isPrime function for input 1")
if not isPrime(2) == True:
    print("Error in isPrime function for input 2")
if not isPrime(7793) == True:
    print("Error in isPrime function for input 7793")
if not isPrime(8000) == False:
    print("Error in isPrime function for input 8000")

# Pigeonhole tests
if not pigeonHole(10, 3) == 4:
    print("Error in pigeonhole function for inputs 10 and 3")
if not pigeonHole(100, 9) == 12:
    print("Error in pigeonhole function for inputs 100 and 9")
if not pigeonHole(1, 1) == 1:
    print("Error in pigeonhole function for inputs 1 and 1")
if not pigeonHole(0, 5) == 0:
    print("Error in pigeonhole function for inputs 0 and 5")

# pigeonHoleReverse tests
if not pigeonHoleReverse(10, 3) == 30:
    print("Error in pigeonHoleReverse function for inputs 10 and 3")
if not pigeonHoleReverse(100, 9) == 900:
    print("Error in pigeonHoleReverse function for inputs 100 and 9")
if not pigeonHoleReverse(1, 1) == 1:
    print("Error in pigeonHoleReverse function for inputs 1 and 1")

# chineseRemainder tests
if not chineseRemainder([3, 5, 7], [2, 3, 2]) == (23, 105):
    print("Error in chineseRemainder function for inputs [3, 5, 7] and [2, 3, 2]")
if not chineseRemainder([4, 9], [3, 8]) == (35, 36):
    print("Error in chineseRemainder function for inputs [4, 9] and [3, 8]")
try:
    _ = chineseRemainder([6, 10, 15], [5, 3, 1])
    print("Error in chineseRemainder function for inputs [6, 10, 15] and [5, 3, 1]")
except ValueError:
    pass  # Expected

# permutation tests
if not permutation(5, 2) == 20:
    print("Error in permutation function for inputs 5 and 2")
if not permutation(3, 2) == 6:
    print("Error in permutation function for inputs 3 and 2")
if not permutation(1, 1) == 1:
    print("Error in permutation function for inputs 1 and 1")
    
