def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())
    answer = smallest(num1, num2)
    print("Smallest: " + str(answer))

def smallest(num1, num2):
    if (num1 < num2):
        return num1
    else:
        return num2

if __name__ == '__main__':
    main()
