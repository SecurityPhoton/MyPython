import math

# ax^2+bx+c=0, so a,b,c will be entered from user input
# One root 1 -6 9
# Two roots 1 -4 -5

# this function should ask user for input, and then return variable. Good to have additional input validation here.
def ask_value(message):
    while True:
        print(message)
        v1 = input()
        try:
            v1 = int(v1)
        except:
            print('Please use numeric digits.')
        break
    return v1



# no much, no less just return discriminant.
def discriminant(a,b,c):
    return pow(b, 2)-4*a*c

# will show on the screen all acceptable roots
def roots(d,a,b,c):
    if d < 0:
        print("No roots!")
    elif d == 0: print("Only one root - " + str(-b/2*a) )
    elif d > 0: 
        print("First root x1 =" + str((-b+math.sqrt(d))/2*a) )
        print(" Second x2 =" + str((-b-math.sqrt(d))/2*a))

# this function should contain inside discriminant and roots functions.
def solv_square(a,b,c):
    roots(discriminant(a,b,c),a,b,c)


# main() here our program will be started, and all required data asked
def main():
    a = ask_value("Enter A:")
    b = ask_value("Enter B:")
    c = ask_value("Enter C:")
    solv_square(a,b,c)

main()
