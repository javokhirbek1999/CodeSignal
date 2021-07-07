def candies(n, m):
    if n == m:
        return n
    remainder = m%n
    return m-remainder
