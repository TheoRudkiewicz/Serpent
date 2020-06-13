from math import exp


def parcours_2xn(n):  # D
    """Parcours(2 x n)"""
    return 2 * (n ** 2 - n + 2)

# genral
def pb_3xn(n):  # D
    """Pb(3 x n)"""
    if n % 2:
        return 2 ** ((n-1) // 2)
    else:
        return 0


def pb_nx3(n):  # D
    """Pb(n x 3)"""
    if n > 1:
        return 2 ** (n - 2)
    elif n == 1:
        return 1
    else:
        raise ValueError(f"{n} n'est pas un entier positif")


def po_nx3(n):  # D
    """Po(n x 3)"""
    if n > 1:
        return 2 ** (n - 2)
    elif n == 1:
        return 1
    else:
        raise ValueError(f"{n} n'est pas un entier positif")


def r(n):  # OK par Pa(3 x n)
    """R(n) pour Pa(3 x n)"""
    if n % 2:  # 2 /| n
        return - n - 1 + 5 * 2 ** ((n -3) // 2)
    else:  # 2 | n
        return - n - 1 + 3 * 2 ** ((n - 2) // 2)


def pa_nx3(n):  # OK 30] w OEIS + D
    """Pa(3 x n)"""
    np = [1]
    for i in range(2, n + 1):
        np.append(sum(np) + i + r(i))
    return np[-1]


def pa_nx3_list(n):  # OK 30] w OEIS + D
    """Pa(3 x n)"""
    np = [1]
    for i in range(2, n + 1):
        np.append(sum(np) + i + r(i))
    return np


# mid
def cas1(n, h):
    if (n - h) % 2:
        return 2 ** ((n - h - 1) // 2) * (sum(pb_3xn(j) + pa_nx3(j) for j in range(1, h - 2 + 1)) + 1)
    else:
        # print('Error')
        return 0


def pmh(n, h):
    """Pour des h entre 2 et n - 1"""
    return cas1(n, h) + cas1(n, n-h+1) + pb_3xn(h-1) * pa_nx3(n-h) + pb_3xn(n-h) * pa_nx3(h-1)


def pm(n):
    """Nombre de parcours pour tout le milieu"""
    # return 2 * sum(pmOh(n, h) for h in range(2, n)) + les hauts
    if n % 4 == 0:  # no
        return 2 * (2 ** (n // 2) + 2 * (cas1(n, n // 2 + 1) + pb_3xn(n // 2 - 1) * pa_nx3(n // 2) + sum(
            cas1(n, n - h + 1) + cas1(n, h + 1) + pb_3xn(h - 1) * pa_nx3(n - h) + pb_3xn(n - h - 1) * pa_nx3(h)
            for h in range(2, n // 2 - 1 + 1, 2))))
    elif n % 4 == 2:  # valide
        return 2 * (2 ** (n // 2) + 2 * sum(
            cas1(n, n - h + 1) + cas1(n, h + 1) + pb_3xn(h - 1) * pa_nx3(n - h) + pb_3xn(n - h - 1) * pa_nx3(h)
            for h in range(2, n // 2 + 1, 2)))
    elif n % 4 == 1:  # valide
        return 4 * (sum(pmh(n, h) for h in range(2, (n - 1) // 2 + 1, 2)))
    else:  # n % 4 == 3, valide
        return 2 * (pmh(n, (n + 1) // 2) + 2 * sum(pmh(n, h) for h in range(2, (n - 1) // 2 - 1 + 1, 2))) 


# cote
# 13
def cas13(n, h):
    if n % 2:
        if h % 2:
            return pa_nx3(n - h) + (h - 1) * pb_3xn(n - h -1)
        else:
            return 0
    else:
        if h % 2:
            return pa_nx3(n - h)
        else:
            return (h + 1) * pb_3xn(n - h - 1)

        
# droite
def pcd_nx3(n, h):  # 2 OK 14]
    """2"""
    # haut + bas (aek cht var)
    return pb_3xn(h - 2) * pa_nx3(n - h) + pb_3xn(n - h - 1) * pa_nx3(h - 1)


# haut
def pcha_nx3(n, h): # 1.1.1.h  NON TESTER
    """1.1"""
    # haut, arrivé libre
    return sum(pb_3xn(n - h - 1) * pa_nx3(k) for k in range(0, h - 2 + 1))


def pcha_ecchelon_nx3(n, h):  # 1.2  NON  TESTER
    """1.2"""
    """après décalage puis redescente espace 2xk àcombler dc ecore pleins de façon"""
    return sum(pb_3xn(k) * cas13(n - k - 1, h - k - 1) for k in range(1, h - 3 + 1))


def pch_nx3(n, h):  # total  OK 14]
    """1"""
    return sum([
        pcha_nx3(n, h),
        pcha_ecchelon_nx3(n, h),
        cas13(n, h)
                ])

# total cote
def pc_nx3(n, h):   # OK 14]
    """haut(1) + bas (haut chgt de var) + droite(2)"""
    return pch_nx3(n, h) + pch_nx3(n, n - h + 1) + pcd_nx3(n, h)



# total
def parcours_3xn(n):
    global pa, pb, p13
    pa = [1] + pa_nx3_list(n)
    pb = [0] + [2 ** ((k - 1) // 2) if k % 2 else 0 for k in range(1, n + 1)]
    p13 = [0] + [cas13(n, h) for h in range(1, n)]
    cote = sum(pc_nx3(n, h) for h in range(2, n))
    return 2 * cote + pm(n) + 4 * pa_nx3(n)


# Fonction de test
def aff_line(m=2, M=20):
    """Fonction de test"""
    for n in range(m, M):
        print("+" * 5, n, '+' * 5)
        print(parcours_3xn(n) // 2)


aff_line()
