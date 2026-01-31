def find_longest_word(*args):
    if not args:
        return 'Нет слов'
    leader = ''
    for word in args:
        if len(word) > len(leader):
            leader = word
    return leader


def remove_from_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, '')
    return string


if __name__ == '__main__':
    print(find_longest_word())
    print(find_longest_word("Python", 'Java', 'Programming'))
    print(remove_from_string('О! Смотри, можно удалить - все знаки препинания сразу!', '?', "!", ",", '.', "-"))
