import msvcrt

def init_screen ():
    print('=======================================')
    print('       Beyond the Veil of Sleep')
    print('=======================================\n')
    print('1 - New Game')
    print('2- Exit')

    option = msvcrt.getch().decode().lower()

    while True:
        if option == '1':
            return 1
        elif option == '2':
            return 0
        else:
            i = 1
            while i <= 3:
                print('>>>>Press a valid option!<<<<')
                print('1 - New Game')
                print('2- Exit')
                option = msvcrt.getch().decode().lower()
                if(option == '1'):
                    return 1
                elif(option == '2'):
                    return 0
                else:
                    print('\n' * 130)
                    print(f'Invalid option.','(',i,'/ 3 )')
                    i = i + 1
                    if (i > 3):
                        print('Too many invalid attempts.')
                        print('Closing...')
        break
