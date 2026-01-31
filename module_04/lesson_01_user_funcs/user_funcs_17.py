def display_planet_address(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    display_planet_address(planet='Earth', star='Sun', galaxy='Milky Way', age=round(4.543e9))
