from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt


def ejercicio_n2():
    lines_1 = []
    with open("1", "r") as f:
        for line in f:
            lines_1.append(int(line.strip().replace("\n", "")))

    lines_2 = []
    with open("2", "r") as f:
        for line in f:
            lines_2.append(int(line.strip().replace("\n", "")))

    lines_3 = []
    for i, j in zip(lines_1, lines_2):
        f = lagrange([0, 1], [i, j])
        lines_3.append(f(0.5))

    print("Lineas 3: ", lines_3)

    time = list(range(130))

    plt.scatter(time, lines_1, c="red")
    plt.scatter(time, lines_2, c="blue")
    plt.scatter(time, lines_3, c="orange")

    plt.show()


def ejercicio_n3():
    lines_1 = []
    with open("1", "r") as f:
        for line in f:
            lines_1.append(int(line.strip().replace("\n", "")))

    lines_2 = []
    with open("2", "r") as f:
        for line in f:
            lines_2.append(int(line.strip().replace("\n", "")))

    lines_3 = []
    with open("3", "r") as f:
        for line in f:
            lines_3.append(int(line.strip().replace("\n", "")))

    lines_4 = []
    for i, j, k in zip(lines_1, lines_2, lines_3):
        f = lagrange([0, 1, 2], [i, j, k])
        lines_4.append(f(1.5))

    print("Lineas 4: ", lines_4)

    time = list(range(130))

    plt.scatter(time, lines_1, c="red")
    plt.scatter(time, lines_2, c="blue")
    plt.scatter(time, lines_3, c="orange")
    plt.scatter(time, lines_4, c="green")
    plt.show()


def main():
    print("Ejercicio N2:")
    ejercicio_n2()
    print("--------------------------------------")
    print("Ejercicio N3:")
    ejercicio_n3()


if __name__ == "__main__":
    main()
