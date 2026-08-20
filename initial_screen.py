import msvcrt

def initial_screen ():
    print('=======================================')
    print('       Beyond the Veil of Sleep')
    print('=======================================\n')
    print('1 - New Game')
    print('2- Exit')

    option = msvcrt.getch().decode().lower()

    while True:
        if option == '1':
            print('iniciar')
            break
        elif option == '2':
            print('exit')
            break
        else:
            i = 1
            while i <= 3:
                print('>>>>Press a valid option!<<<<')
                print('1 - New Game')
                print('2- Exit')
                option = msvcrt.getch().decode().lower()
                if(option == '1'):
                    print('iniciar')
                    break
                elif(option == '2'):
                    print('exit')
                    break
                else:
                    print('\n' * 130)
                    print(f'Invalid option.','(',i,'/ 3 )')
                    i = i + 1
                    if (i > 3):
                        print('Too many invalid attempts.')
                        print('Closing...')
        break

def main():
    initial_screen()

if __name__ == "__main__":
    main()
