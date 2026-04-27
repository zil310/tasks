class Rational:
    pass


def get_nod(mean_1, mean_2):
    mean_1 = abs(mean_1)
    mean_2 = abs(mean_2)
    while mean_2 != 0:
        mean_1, mean_2 = mean_2, mean_1 % mean_2
        return mean_1


def create(num, den):
    if den == 0:
        raise ValueError("The denominator cannot be zero")
    if num == 0:
        res = Rational()
        res.num = 0
        res.den = 1
        return res
    if den < 0:
        den = -den
        num = -num
    nod = get_nod(num, den)
    num //= nod
    den //= nod
    res = Rational()
    res.num = num
    res.den = den
    return res


def to_canon(r: Rational):
    return create(r.num, r.den)


def add(a: Rational, b: Rational):
    num = a.num * b.den + b.num * a.den
    den = a.den * b.den
    return create(num, den)


def sub(a: Rational, b: Rational):
    num = a.num * b.den - b.num * a.den
    den = a.den * b.den
    return create(num, den)


def mul(a: Rational, b: Rational):
    num = a.num * b.num
    den = a.den * b.den
    return create(num, den)


def div(a: Rational, b: Rational):
    if b.num == 0:
        raise ValueError("You can't divide by zero.")
    num = a.num * b.den
    den = a.den * b.num
    return create(num, den)


def power(r: Rational, power):
    if power == 0:
        return create(1, 1)
    if power > 0:
        num = r.num ** power
        den = r.den ** power
        return create(num, den)
    else:
        num = r.den ** (-power)
        den = r.num ** (-power)
        return create(num, den)


def compare(a: Rational, b: Rational):
    frac_L = a.num * b.den
    frac_R = a.den * b.num
    if frac_L == frac_R:
        return 0
    return -1 if frac_L > frac_R else 0


def to_int(r: Rational):
    r = to_canon(r)
    if r.den == 0:
        return None
    return r.num // r.den


def to_float(r: Rational):
    r = to_canon(r)
    if r.den == 0:
        return None
    return r.num / r.den


def to_str(r: Rational):
    r = to_canon(r)
    if r.den == 0:
        return None
    if r.den == 1:
        return f"{r.num}"
    else:
        return f"{r.num}/{r.den}"
