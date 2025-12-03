from typing import TypedDict
from math import sqrt, floor

class GraphProperties(TypedDict, total=False):
    vertices: int
    edges: int
    degree: list[int]
    error: str

def gcd(num1: int, num2: int) -> int:
    """Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        int: The GCD of the two integers.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return abs(num1)

def gcd_bezout(num1: int, num2: int) -> tuple[int, int, int]:
    """Compute the GCD of two integers and the coefficients for Bézout's identity.

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        tuple[int, int, int]: A tuple containing the GCD and the coefficients (x, y) such that
                              GCD = x * num1 + y * num2.
    """
    old_r, r = num1, num2
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def isCoprime(num1: int, num2: int) -> bool:
    """Check if two integers are coprime (i.e., their GCD is 1).

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        bool: True if the integers are coprime, False otherwise.
    """
    return gcd(num1, num2) == 1

def graphProperties(n: int, graph_type: str) -> GraphProperties:
    """Return properties of an n-graph based on its type.

    Args:
        n (int): The number of vertices in the graph.
        graph_type (str): The type of the graph.
        Supported types: 'complete', 'cube', 'cycle', 'wheel'.

    Returns:
        dict: A dictionary containing properties of the graph.
    """
    properties: GraphProperties = {}
    if graph_type == 'complete':
        properties['vertices'] = n
        properties['edges'] = n * (n - 1) // 2
        properties['degree'] = [n - 1] * n
    
    elif graph_type == 'cube':
        properties['vertices'] = 2 ** n
        properties['edges'] = n * (2 ** (n - 1))
        properties['degree'] = [n] * (2 ** n)
    
    elif graph_type == 'cycle':
        if n < 3:
            properties['error'] = 'A cycle graph must have at least 3 vertices'
        else:
            properties['vertices'] = n
            properties['edges'] = n
            properties['degree'] = [2] * n
    
    elif graph_type == 'wheel':
        if n < 4:
            properties['error'] = 'A wheel graph must have at least 4 vertices'
        else:
            properties['vertices'] = n
            properties['edges'] = 2 * (n - 1)
            properties['degree'] = [n - 1] + [3] * (n - 1)
    
    else:
        properties['error'] = 'Unknown graph type'
    return properties

def inclusion_exclusion(sets: int, size: int, overlaps: list[int]) -> int:
    """Calculate the size of the union of n sets using the inclusion-exclusion principle.

    Args:
        sets (int): The number of sets.
        size (int): The size of each individual set. Must be the same for all sets.
        overlaps (list[int]): A list containing the sizes of the intersections of the sets.
                            The first element is the size of pairwise intersections,
                            the second is for triple intersections, and so on.
    
    Returns:
        int: The size of the union of the sets.
        
    Example:
        For 4 sets of size 200 with pairwise overlaps of 50, triple overlaps of 25, and quadruple overlaps of 5,
        inclusion_exclusion(4, 200, [50, 25, 5]) returns 595
    """
    n = sets
    total = n * size  # Start with the sum of individual set sizes

    # Subtract pairwise intersections
    if n >= 2:
        total -= overlaps[0] * (n * (n - 1) // 2)

    # Add triple intersections
    if n >= 3:
        total += overlaps[1] * (n * (n - 1) * (n - 2) // 6)

    # Subtract quadruple intersections
    if n >= 4:
        total -= overlaps[2] * (n * (n - 1) * (n - 2) * (n - 3) // 24)

    return total

def choose(n: int, k: int) -> int:
    """Calculate the binomial coefficient "n choose k".

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The binomial coefficient.
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

def binom(n: int, k: int) -> int:
    
    """Alias for choose function to calculate binomial coefficient.

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose.

    Returns:
        int: The binomial coefficient.
    """
    return choose(n, k)

def derange(n: int) -> int:
    """Calculate the number of derangements (permutations where no element appears in its original position) of n items.

    Args:
        n (int): The number of items.

    Returns:
        int: The number of derangements.
    """
    if n < 0:
        return -1  # Undefined for negative numbers
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        derangements = [0] * (n + 1)
        derangements[0] = 1
        derangements[1] = 0
        derangements[2] = 1
        for i in range(3, n + 1):
            derangements[i] = (i - 1) * (derangements[i - 1] + derangements[i - 2])
        return derangements[n]

def primesUnder(n: int) -> list[int]:
    """Return a list of all prime numbers less than or equal to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit.
    Returns:
        list[int]: A list of prime numbers less than or equal to n.
    """
    
    sqrt_n: int = floor(sqrt(n))
    
    sieve = [True] * n
    if n > 0:
        sieve[0] = False
    if n > 1:
        sieve[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(sqrt_n) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    return [i for i in range(n) if sieve[i]]

def isPrime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def pigeonHole(items: int, boxes: int) -> int:
    """Calculate the minimum number of items that must be in at least one box using the pigeonhole principle.

    Args:
        items (int): The total number of items.
        boxes (int): The total number of boxes.

    Returns:
        int: The minimum number of items in at least one box.
    """
    if boxes <= 0:
        raise ValueError("Number of boxes must be greater than zero.")
    return (items + boxes - 1) // boxes  # Equivalent to ceil(items / boxes)

def pigeonHoleReverse(noMoreThan: int, boxes: int) -> int:
    """Calculate the maximum number of items that can be placed in boxes without exceeding a specified limit in any box.

    Args:
        noMoreThan (int): The maximum number of items allowed in any box.
        boxes (int): The total number of boxes.

    Returns:
        int: The maximum number of items that can be placed in the boxes.
    """
    if noMoreThan < 0:
        raise ValueError("The maximum number of items per box must be non-negative.")
    if boxes < 0:
        raise ValueError("The number of boxes must be non-negative.")
    return noMoreThan * boxes

def chineseRemainder(the_moduli: list[int], the_remainders: list[int]) -> tuple[int, int]:
    """Solve a system of simultaneous congruences using the Chinese Remainder Theorem.

    Args:
        the_moduli (list[int]): A list of pairwise coprime moduli.
        the_remainders (list[int]): A list of remainders corresponding to each modulus.

    Returns:
        tuple[int, int]: A tuple containing the solution and the product of the moduli.
        [solution, product_of_moduli]
    """
    for modulus in the_moduli:
        if modulus <= 0:
            raise ValueError("Moduli must be positive integers.")
    if len(the_moduli) != len(the_remainders):
        raise ValueError("The number of moduli must equal the number of remainders.")
    
    
    prod = 1
    for modulus in the_moduli:
        prod *= modulus

    result = 0
    for modulus, remainder in zip(the_moduli, the_remainders):
        partial_prod = prod // modulus
        gcd_value, inverse, _ = gcd_bezout(partial_prod, modulus)
        if gcd_value != 1:
            raise ValueError("Moduli must be pairwise coprime.")
        result += remainder * inverse * partial_prod

    return result % prod, prod

def permutation(n: int, k: int) -> int:
    """Calculate the number of permutations of n items taken k at a time.

    Args:
        n (int): The total number of items.
        k (int): The number of items to arrange.

    Returns:
        int: The number of permutations.
    """
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(k):
        result *= n - i
    return result