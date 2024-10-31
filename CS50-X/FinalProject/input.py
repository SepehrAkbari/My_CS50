import numpy as np

def grid(n):
    # example
    m_ex = [
        [0, 6, 4, 0, 0, 2, 0, 0, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 7],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 8, 0, 0, 9, 6, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 3, 8, 2, 0, 0, 9, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 1],
        [7, 0, 0, 0, 0, 9, 0, 0, 4],
        [0, 0, 0, 3, 0, 0, 5, 8, 0]
    ]
    # unsolvable
    m_na = [
        [1, 2, 3, 4, 5, 6, 7, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9]
    ]

    # input
    m = [
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]
    ]

    if n == 1:
        return m_ex
    elif n == 2:
        return m_na
    elif n == 3:
        return m
    else:
        print("Invalid grid code")

def printGrid(m):
    print(np.matrix(m))


def main():
    pass

if __name__ == "__main__":
    main()
