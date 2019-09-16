if __name__ == '__main__':

    birthdays = {
        'Walt Disney': '12/05/1901',
        'Alex Hirsch': '06/18/1985',
        'Mark Fishbach': '06/28/1989',
        'Roger Clark': '03/16/1981',
        'Kermit the Frog': '05/9/????'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
        print("Would you like to tell me their birthday? I'll try to remember in the future!")
        name = input()
        print("Thank you! Maybe in the future we will update our dictionary with your addition.")