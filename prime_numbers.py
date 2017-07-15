import math

def is_prime(n):
    """ KEATONS EPIC PRIME FUNCTION
    This function takes a single integer and returns True if prime and False if not
    """
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

found_primes = 0
current_number = 2000
lower_limit = 0
upper_limit = 0
max_found = 0
num_selection = 0
done = False



while(not done):
    print ""
    print "Current lower limit: " + str(lower_limit)
    print "Current upper limit: " + str(upper_limit)
    print "Max amount of primes you want found: " + str(max_found)
    print ""
    print "Hit '1' to set upper limit"
    print "Hit '2' to set lower limit"
    print "Hit '3' to set max amount of primes you want found"
    print "Hit '4' to find primes"
    print ""
    num_selection = raw_input("Enter choice: ")

    if num_selection == "1":
        upper_limit = int(raw_input("Select upper limit: "))
    elif num_selection == "2":
        lower_limit = int(raw_input("Select lower limit: "))
    elif num_selection == "3":
        max_found = int(raw_input("Select amount of primes you want to find: "))
    elif num_selection == "4":
        done = True


while (current_number >= lower_limit and current_number <= upper_limit) and (found_primes < max_found):
    if (is_prime(current_number)):
        print current_number
        found_primes = found_primes + 1
    current_number = current_number + 1


user_out = "We found: " + str(found_primes) + " primes"

print user_out

raw_input("Press any key to continue...")