def MultiTabl():
    tabl = "".join(
        ["".join([f"{x*y}\t" for x in range(1, 11)]) + "\n" for y in range(1, 11)]
    )
    return tabl
