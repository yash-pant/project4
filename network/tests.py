#from django.test import TestCase

# Create your tests here.
count = 0
cv = 0
TestCase = 0
abcd = 0
running = True
while running:    
    t = input('Type "Quit" whenever you want to quit out of the loop: ')
    cv += 1
    TestCase -= 10
    count += 1
    if t == "Quit" or t == "QUIT" or t == "quit":
        print("you have exited the loop. Goodbye...")
        break
    else:
        if count <= 5 and TestCase >= -20:
            print("20")
        elif cv == 7:
            abcd += 90 
            print(abcd)
        else:
            print("Error 404 page not found.")

if count <= 5:
    print("you exited at only " + str(count) + " times ...was there a problem with your service?")
    c = input()
elif count > 5 and count <= 14:
    print("Were you satisfied with your service?")
    s = input()
elif count > 15:
    print("you stayed in the loop for " + str(count) + " counts, were you afk?")
    a = input()
else:
    print("Bad input please try again")

while running:
    name = input("What is your NAME????? ")
    print("HELLOW " + name)
    yes = input("If I said your name correctly say 'yes' ")
    if yes == "yes":
        print("ok thank you")
        break
    else:
        print("I'm sorry I got your name wrong")
        print("lets try again shall we...")

while running:
    print("Ha you got stuck in an infinite loop")
    print('HAAAAAAA' * 1000000)
    print("You are never getting out")
    print('HAAAAAAA' * 1000000)
    q = input()
    if q == "quit" or q == "QUIT" or q == "Quit":
        break

print("You have successfully left the loop...")
print("Heres your prize: ")
print("You have been gifted 50000000 bits congrats you're rich.")