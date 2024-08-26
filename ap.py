def AP():
    while True:
        try:
            while True:
                try:
                    a = int(input("\nEnter the starting number=> "))  # Start of the sequence
                    break
                except Exception as e:
                    print(f'\nerror occured:{e}')
                    continue
            while True:
                try:
                    n = int(input("\nEnter the last number=> "))  # End of the sequence
                    break
                except Exception as e:
                    print(f'\nerror occured:{e}')
                    continue
            while True:
                try:
                    d = int(input("\nEnter the common difference=> "))  # Common difference
                    if d == 0:
                        print("\nInvalid value for common difference.")
                        continue
                    break
                except Exception as e:
                    print(f'\nerror occured:{e}')
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
            
            print(f"\nSequence: {sequence}")
            print(f"\nTotal sum = {sum}")

        except ValueError:
            print("Please enter valid integers.")
        finally:
            ask=input("Want to try again? enter [Y/y]=> ")
            if ask.lower()=="y":
                continue
            print("thank you")
            break
AP()
