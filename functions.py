def count_primes(num):

    for i in range(0, num+1):

        if i > 1:

            for j in range(2, i):
                if i % j == 0:
                    #  4 % 3 = 1
                    # True or False
                    break

            else:
                print(i)


count_primes(100)
