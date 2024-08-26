import colorama as c
c.init

()
def AP():
    while True:
        try:
            while True:
                try:
                    a = int(input(f"\n{c.Fore.GREEN}Enter the starting number=> {c.Fore.RESET}"))  # Start of the sequence
                    break
                except Exception as e:
                    print(f'{c.Fore.RED}\nerror occured:{e}{c.Fore.RESET}')
                    continue
            while True:
                try:
                    n = int(input(f"\n{c.Fore.GREEN}Enter the last number=> {c.Fore.RESET}"))  # End of the sequence
                    break
                except Exception as e:
                    print(f'{c.Fore.RED}\nerror occured:{e}{c.Fore.RESET}')
                    continue
            while True:
                try:
                    d = int(input(f"\n{c.Fore.GREEN}Enter the common difference=> {c.Fore.RESET}"))  # Common difference
                    if d == 0:
                        print(f"\n{c.Fore.LIGHTRED_EX}Invalid value for common difference.{c.Fore.RESET}")
                        continue
                    break
                except Exception as e:
                    print(f'{c.Fore.RED}\nerror occured:{e}{c.Fore.RESET}')
                    continue



            
            sum = 0
            sequence = []

            if d > 0:
                for i in range(a, n + 1, d):
                    sum += i
                    sequence.append((i))
            else:
                for i in range(a, n - 1, d):
                    sum += i
                    sequence.append((i))
            
            print(f"\n{c.Fore.LIGHTMAGENTA_EX}Sequence: {c.Fore.RESET}{sequence}")
            print(f"\n{c.Fore.LIGHTMAGENTA_EX}Total sum = {c.Fore.RESET}{sum}")

        except ValueError:
            print(f"{c.Fore.RED}\nerror occured:{e}{c.Fore.RESET}")
        finally:
            ask=input(f"{c.Fore.LIGHTBLUE_EX}Want to try again? enter [Y/y]=> {c.Fore.RESET}")
            if ask.lower()=="y":
                continue
            print(f"{c.Fore.LIGHTBLUE_EX}thank you{c.Fore.RESET}")
            break
AP()
