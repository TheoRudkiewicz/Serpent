import numpy as np
from time import perf_counter as perf
from numba import jit


@jit(nopython=True)
def count_in_matrice(matrice, x, y, n):
    if not n:
        return 1
    else:
        result = 0
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            try:
                if (not matrice[x + dx][y + dy]) and x + dx >= 0 and y + dy >= 0:
                    # print(x + dx, y + dy)
                    matrice[x + dx][y + dy] = True
                    result += count_in_matrice(matrice, x + dx, y + dy, n - 1)
                    matrice[x + dx][y + dy] = False
            except IndexError:
                pass
        return result


def walkeur(matrice, x, y):
    matrice[x][y] = True
    r = count_in_matrice(matrice, x, y, matrice.shape[0] * matrice.shape[1] - 1)
    matrice[x][y] = False
    return r
    


def count_path(Lx, ly):
    """Fait tt les points de départ possibles"""
    nodes = np.full((Lx, ly), False)
    total = 0
    if Lx % 2:  # impair
        if ly % 2:  # impair
            for x in range(0, Lx // 2):
                for y in range(0, ly // 2):
                    if not (x + y) % 2:  # th parite
                        dt = total
                        total += 4 * walkeur(nodes, x, y)
                        # print('Aii', coord_value(x, y, ly), (total - dt) // 4)
            for y in range(0, ly // 2):
                if not (Lx // 2 + y) % 2:
                    dt = total
                    total += 2 * walkeur(nodes, Lx // 2, y)
                    # print('Cxii', y, coord_value(Lx // 2, y, ly), (total - dt) // 2)
            for x in range(0, Lx // 2):
                if not (ly // 2 + x) % 2:
                    dt = total
                    total += 2 * walkeur(nodes, x, ly // 2)
                    # print('Cyii', x, coord_value(x, ly // 2, ly), (total - dt) // 2)
            if not (Lx // 2 + ly // 2) % 2:
                dt = total
                total += walkeur(nodes, Lx // 2, ly // 2)
                # print('Mii', coord_value(Lx // 2, ly // 2, ly), total - dt)
        else:  # ly pair
            for x in range(0, Lx // 2):
                for y in range(0, ly // 2):
                    dt = total
                    total += 4 * walkeur(nodes, x, y)
                    # print('A', coord_value(x, y, ly), (total - dt) // 4)
            for y in range(0, ly // 2):
                dt = total
                total += 2 * walkeur(nodes, Lx // 2, y)
                # print('Cxip', y, coord_value(Lx // 2, y, ly), (total - dt) // 2)
    else:  # Lx pair
        if ly % 2:  # impair
            for x in range(0, Lx // 2):
                for y in range(0, ly // 2):
                    dt = total
                    total += 4 * walkeur(nodes, x, y)
                    # print('Api', coord_value(x, y, ly), (total - dt) // 4)
            for x in range(0, Lx // 2):
                dt = total
                total += 2 * walkeur(nodes, x, ly // 2)
                # print('Cypi', x, coord_value(x, ly // 2, ly), (total - dt) // 2)
        else:
            for x in range(0, Lx // 2):
                for y in range(0, ly // 2):
                    dt = total
                    total += 4 * walkeur(nodes, x, y)
                    # print('App', coord_value(x, y, ly), (total - dt) // 4)
    return total



if __name__ == '__main__':
    for n in range(1):
         t = perf()
         nodes = np.full((3, 8), False)
         print(n, walkeur(nodes, 0, 0), perf() - t)
