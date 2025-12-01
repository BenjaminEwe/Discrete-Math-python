from typing import TypedDict

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




