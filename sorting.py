def draw_list(L: list) -> None:
    import os

    # fixes ANSI codes on Windows
    # an explanation can be found here: https://bugs.python.org/msg291732
    os.system('')

    print("\033[H", end='') # move cursor to (0,0)
    print("\033[0J", end='') # erase screen
    output = ""
    M = max(L)
    for line_index in range(1, M+1):
        line = ""
        for height in L:
            if line_index <= height:
                line += '|'
            else:
                line += ' '
        line += '\n'
        output = line + output
    print(output)


def bubble_sort(L: list, draw: bool = False) -> None:
    for k in range(1, len(L)):
        for index in range(len(L)-k):
            if L[index] > L[index+1]:
                L[index], L[index+1] = L[index+1], L[index]
            if draw:
                draw_list(L)


def _insert(L: list, index: int, draw: bool = False) -> None:
    key = L[index]
    while index > -1 and key <= L[index]:
        L[index] = L[index-1]
        index -= 1
        if draw:
            draw_list(L)
    L[index+1] = key
    if draw:
        draw_list(L)

def insert_sort(L: list, draw: bool = False) -> None:
    for ind in range(len(L)):
        _insert(L, ind, draw)


def _selection(L: list, begin: int, draw: bool = False) -> int:
    imin = begin
    for i in range(begin, len(L)):
        if L[i] < L[imin]:
            imin = i
        if draw:
            draw_list(L)
    return imin

def selection_sort(L: list, draw: bool = False) -> None:
    for i in range(len(L)):
        imin = _selection(L, i, draw)
        L[i], L[imin] = L[imin], L[i]


def quick_sort(L: list) -> list:
    # this one doesn't get the luxury of visual representation
    # because I can't figure out how to do that with a recursive algorithm without summoning some eldritch horrors along the way
    if len(L) < 2:
        return L

    pivot = L[-1]
    l, r = [], []
    for element in L[:-1]:
        if element < pivot:
            l += [element]
        else:
            r += [element]

    return quick_sort(l) + [pivot] + quick_sort(r)
