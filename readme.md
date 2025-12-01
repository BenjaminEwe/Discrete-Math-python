# Discrete Math Helper Commands

| Command | Description | Syntax (Python) | Example Output |
| --- | --- | --- | --- |
| `gcd(a, b)` | Greatest common divisor via Euclid. | `gcd(84, 126)` | `42` |
| `gcd_bezout(a, b)` | GCD plus Bézout coefficients. | `gcd_bezout(154, 48)` | `(2, 5, -16)` |
| `isCoprime(a, b)` | Checks if two integers are coprime. | `isCoprime(35, 64)` | `True` |
| `graphProperties(n, kind)` | Basic stats for `complete`, `cube`, `cycle`, `wheel`. | `graphProperties(5, "wheel")` | `{'vertices': 5, 'edges': 8, 'degree': [4, 3, 3, 3, 3]}` |
| `inclusion_exclusion(k, size, overlaps)` | Union size via inclusion–exclusion. | `inclusion_exclusion(4, 200, [50, 25, 5])` | `595` |
| `choose(n, k)` / `binom(n, k)` | Binomial coefficients. | `choose(10, 3)` | `120` |
| `derange(n)` | Derangements count for *n* items. | `derange(6)` | `265` |