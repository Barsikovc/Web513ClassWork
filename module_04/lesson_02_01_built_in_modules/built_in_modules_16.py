from platform import processor
from multiprocessing import Pool


def square(x):
    return x ** 2


if __name__ == '__main__':
    print(processor())

    user_pc = {
        "AMD64 Family 25 Model 33 Stepping 2, AuthenticAMD": {'cores': 8, 'threads': 16}
    }
    cores = user_pc[processor()]['cores']
    with Pool(processes=cores) as pool:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        results = pool.map(square, numbers)

    print(f'Квадраты чисел: {results}')
