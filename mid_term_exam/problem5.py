def discriminant(a, b, c):
    return b * b - 4 * a * c

def quadratic(a, b, c):
    disc = discriminant(a, b, c)
    if disc < 0:
        return None
    s1 = (- b - disc ** (1 / 2)) / (2 * a)
    s2 = (- b + disc ** (1 / 2)) / (2 * a)
    return (s1, s2)