from discrete import *

#GCD tests
if not GCD(48, 18) == 6:
    print("Error in GCD function for inputs 48 and 18")
if not GCD(101, 10) == 1:
    print("Error in GCD function for inputs 101 and 10")
if not GCD(270270, 18) == 18:
    print("Error in GCD function for inputs 270270 and 18")
if not GCD(705705, 18) == 3:
    print("Error in GCD function for inputs 705705 and 18")

#GCD_bezout tests
if not GCD_bezout(48, 18) == (6, -1, 3):
    print("Error in GCD_bezout function for inputs 48 and 18")
if not GCD_bezout(101, 10) == (1, 1, -10):
    print("Error in GCD_bezout function for inputs 101 and 10")
if not GCD_bezout(270270, 18) == (18, 0, 1):
    print("Error in GCD_bezout function for inputs 270270 and 18")
if not GCD_bezout(705705, 18) == (3, -1, 39206):
    print("Error in GCD_bezout function for inputs 705705 and 18")

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
    