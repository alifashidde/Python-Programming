import numpy as np
import matplotlib.pyplot as plt
import itertools  # imports the itertools module to generate possible partitions

def random(size):
    # generate random numbers between the given cardinalities
    rand_nums = [np.random.randint(size * 10, size * 100) for _ in range(size)]
    print("\n\nS: ", rand_nums)
    return rand_nums

def idealSum(random_numbers):
    ideal_sum = sum(random_numbers) / 2  # calculates the ideal sum
    print("IDEAL SUM: ", ideal_sum)
    return ideal_sum

def sums(s1):
    sum_first_half=sum(s1)   # calculates all the sums needed
    return sum_first_half

def deviations(S1):
    deviation=abs(S1-ideal_Sum)  # calculates the deviation
    return deviation

def methodA(random_numbers):
    print("PART A")
    # split the list of random numbers in half
    half = len(random_numbers) // 2
    list1 = random_numbers[:half]  # used in getting the first half of the list
    list2 = random_numbers[half:]  # used in getting the second half of the list

    # print the lists of the two partition
    print("S1: ", list1)
    print("S2: ", list2)
    return list1

def methodB(random_numbers):
    print("PART B")

    # split the list of random numbers into even and odd array indices
    even_nums = [random_numbers[i] for i in range (len(random_numbers)) if i % 2 == 0] # checks if number is even
    odd_nums = [random_numbers[i] for i in range (len(random_numbers)) if i % 2 != 0]  # checks if number is odd
    # print the two partitions   
    print("S1: ", even_nums)
    print("S2: ", odd_nums)
    return even_nums

def methodC(random_numbers):
    print("PART C")
    # split the list of random numbers into even and odd numbers
    for i in range(2):
        # this creates empty arrays for odd and even numbers
        even_num = []
        odd_num = []
        # this iterate over the list and append every number to its appropriate list
        for num in random_numbers:
            if num % 2 == 0: # check if number is even
               even_num.append(num) # this adds the number to even list
            else:
               odd_num.append(num) # add number to odd list
        # print the results
        print("S1: ", even_num)
        print("S2: ", odd_num)
        return even_num


def methodD(random_numbers):
    print("PART D")
    s1, s2 =[], []
    sum1, sum2 = random_numbers[0], random_numbers[1]
    # iterates over remaining numbers in the list and add them to the partition with the smallest sum
    for n in range(0,len(random_numbers)):
        if sum1 < sum2:
            s1.append(random_numbers[n])
            sum1 += random_numbers[n]
        else:
            s2.append(random_numbers[n])
            sum2 += random_numbers[n]
            # print the results
    print(s1)
    print(s2)
    return s1

def methodE(random_numbers):
    print("PART E")
    sort=sorted(random_numbers) # this sorts the numbers in ascending order
    print("SORTED S: ", sort)
    even_nums1 = [sort[i] for i in range (len(sort)) if i % 2 == 0] # check if number in sorted list is even
    odd_nums1 = [sort[i] for i in range (len(sort)) if i % 2 != 0]  # check if number in sorted list is not even
    # print the results
    print("S1: ", even_nums1)
    print("S2: ", odd_nums1)
    return even_nums1

def methodF(random_numbers):
    print("PART F")
    sort1=sorted(random_numbers) # this sorts the numbers in ascending order
    print("SORTED S: ", sort1)
    s11, s22 = [], [] # creates empty arrays for even and odd array indices
    sum11, sum22 = random_numbers[0], random_numbers[1]
    # iterates over remaining numbers in the list and add them to the partition with the smallest sum
    for r in range(0,len(random_numbers)):
        if sum11 < sum22:
            s11.append(random_numbers[r]) # appends even array indices to the array s11
            sum11 += random_numbers[r]
        else:
            s22.append(random_numbers[r]) # append odd array indices to the array s22
            sum22 += random_numbers[r]
    # print the results
    print(s11)
    print(s22)
    return s11

def methodG(random_numbers):

    print("PART G")
    sort2=sorted(random_numbers, reverse=True) # sorts the numbers in descending order
    print("SORTED S: ", sort2)
    s111, s222 = [], [] # creates empty arrays for even and odd array indices
    sum111, sum222 = random_numbers[0], random_numbers[1]
    # iterates over remaining numbers in the list and add them to the partition with the smallest sum
    for r in range(0,len(random_numbers)):
        if sum111 < sum222:
            s111.append(random_numbers[r]) # appends even array indices to the array s111
            sum111 += random_numbers[r]
        else:
            s222.append(random_numbers[r]) # append odd array indices to the array s222
            sum222 += random_numbers[r]
    # print results
    print(s111)
    print(s222)
    return s111

def methodH(random_numbers, idealsum):

    print("PART H")
    # variables for best partition and deviation
    best_partition = None
    best_deviation = float('inf')
    # iterate through the numbers using two-way partitions
    for partition in itertools.combinations(random_numbers, len(random_numbers ) // 2):
        # calculate deviation of every partition form ideal sum
        deviation = abs(sum(partition) - idealsum)
        # this updates the best partition a =nd its deviation if the current partition has lower deviation
        if deviation < best_deviation:
            best_partition = partition
            best_deviation = deviation
    # print output
    print("Best partition:", best_partition)
    print("Deviation from ideal:", best_deviation)
    return best_deviation

def methodI(random_numbers, ideal_Sum, algorithmA):

    print("PART I")
    # initialize max_sum to negetive infinity
    max_sum = float('-inf')
    current_sum = 0  # initialize current_sum to 0
    # iterate over each element of the array
    for m in algorithmA:
        current_sum += m  # add current element to current_sum
        max_sum = max(max_sum, current_sum)  # update max_sum to max of current value
        if current_sum < 0:
            current_sum = 0
    print("Maximum sum in the partition: ", max_sum)
    difference = ideal_Sum-max_sum  # calculate difference between ideal sum and max_sum
    print("Lowest difference: ", difference)
    return difference



meanA = []
meanB = []
meanC = []
meanD = []
meanE = []
meanF = []
meanG = []
meanH = []
meanI = []
     # TEST OF HARNESS

sizes = [8, 16, 32, 64, 128, 256, 512, 1024]  # array sizes for the code
for size in sizes:
    # empty lists for storing deviation
    devA = []
    devB = []
    devC = []
    devD = []
    devE = []
    devF = []
    devG = []
    devH = []
    devI = []
    # loops the code 1000 times
    for i in range(1000):
        random_numbers=random(size)                 # function that generates random numbers
        ideal_Sum=idealSum(random_numbers)          # function that calculates ideal sum

        algorithmA = methodA(random_numbers)       # function of algorithm A
        sumA = sums(algorithmA)                    # sums the variable returned(first half) in algorithm A
        devA.append(deviations(sumA))               # append the deviation to the empty list

        algorithmB = methodB(random_numbers)        # function of algorithm B
        sumB = sums(algorithmB)                     # sums the variable returned(first half) in algorithm B
        devB.append(deviations(sumB))               # append the deviation to the empty list

        algorithmC = methodC(random_numbers)        # function of algorithm C
        sumC = sums(algorithmC)                     # sums the variable returned(first half) in algorithm C
        devC.append(deviations(sumC))               # append the deviation to the empty list

        algorithmD = methodD(random_numbers)        # function of algorithm D
        sumD = sums(algorithmD)                     # sums the variable returned(first half) in algorithm D
        devD.append(deviations(sumD))               # append the deviation to the empty list

        algorithmE = methodE(random_numbers)        # function of algorithm E
        sumE = sums(algorithmE)                     # sums the variable returned(first half) in algorithm E
        devE.append(deviations(sumE))               # append the deviation to the empty list

        algorithmF = methodF(random_numbers)        # function of algorithm F
        sumF = sums(algorithmF)                     # sums the variable returned(first half) in algorithm F
        devF.append(deviations(sumF))               # append the deviation to the empty list

        algorithmG = methodG(random_numbers)        # function of algorithm G
        sumG = sums(algorithmG)                     # sums the variable returned(first half) in the algorithm G
        devG.append(deviations(sumG))               # append the deviation to empty list

        #algorithmH = methodH(random_numbers, ideal_Sum)  # function of algorithm H
       # devH.append(algorithmH)                          # append the deviation to the empty list

        algorithmI = methodI(random_numbers, ideal_Sum, algorithmA)  # function of algorithm I
        devI.append(methodI(random_numbers, ideal_Sum, algorithmA))        # append the deviation to the empty list



    calculate_meanA = np.mean(devA)  # calculates mean deviations devA
    calculate_meanB = np.mean(devB)  # calculates mean deviations devB
    calculate_meanC = np.mean(devC)  # calculates mean deviations devC
    calculate_meanD = np.mean(devD)  # calculates mean deviations devD
    calculate_meanE = np.mean(devE)  # calculates mean deviations devE
    calculate_meanF = np.mean(devF)  # calculates mean deviations devF
    calculate_meanG = np.mean(devG)  # calculates mean deviations devG
   # calculate_meanH = np.mean(devH)  # calculates mean deviations devH
    calculate_meanI = np.mean(devI)  # calculates mean deviations devI

    meanA.append(calculate_meanA)  # append the corresponding mean to meanA
    meanB.append(calculate_meanB)  # append the corresponding mean to meanB
    meanC.append(calculate_meanC)  # append the corresponding mean to meanC
    meanD.append(calculate_meanD)  # append the corresponding mean to meanD
    meanE.append(calculate_meanE)  # append the corresponding mean to meanE
    meanF.append(calculate_meanF)  # append the corresponding mean to meanF
    meanG.append(calculate_meanG)  # append the corresponding mean to meanG
   # meanH.append(calculate_meanH)  # append the corresponding mean to meanH
    meanI.append(calculate_meanI)  # append the corresponding mean to meanI

    print(meanA)
    print(meanB)
    print(meanC)
    print(meanD)
    print(meanE)
    print(meanF)
    print(meanG)
    #print(meanH)
    print(meanI)

x = sizes
errorA = np.std(meanA)/np.sqrt(len(meanA))  # calculates error bar for meanA
errorB = np.std(meanB)/np.sqrt(len(meanB))  # calculates error bar for meanB
errorC = np.std(meanC)/np.sqrt(len(meanC))  # calculates error bar for meanC
errorD = np.std(meanD)/np.sqrt(len(meanD))  # calculates error bar for meanD
errorE = np.std(meanE)/np.sqrt(len(meanE))  # calculates error bar for meanE
errorF = np.std(meanF)/np.sqrt(len(meanF))  # calculates error bar for meanF
errorG = np.std(meanG)/np.sqrt(len(meanG))  # calculates error bar for meanG
#errorH = np.std(meanH)/np.sqrt(len(meanH))  # calculates error bar for meanH
errorI = np.std(meanI)/np.sqrt(len(meanI))  # calculates error bar for meanI

plt.errorbar(x, meanA, yerr=errorA, label='taskA')   # plots meanA against x and labels it taskA
plt.errorbar(x, meanB, yerr=errorB, label='taskB')   # plots meanB against x and labels it taskB
plt.errorbar(x, meanC, yerr=errorC, label='taskC')   # plots meanC against x and labels it taskC
plt.errorbar(x, meanD, yerr=errorD, label='taskD')   # plots meanD against x and labels it taskD
plt.errorbar(x, meanE, yerr=errorE, label='taskE')   # plots meanE against x and labels it taskE
plt.errorbar(x, meanF, yerr=errorF, label='taskF')   # plots meanF against x and labels it taskF
plt.errorbar(x, meanG, yerr=errorG, label='taskG')   # plots meanG against x and labels it taskG
#plt.errorbar(x, meanH, yerr=errorH, label='taskH')   # plots meanH against x and labels it taskH
plt.errorbar(x, meanI, yerr=errorI, label='taskI')   # plots meanI against x and labels it taskI
# legend and labels are set
plt.xlabel('Cardinalities')
plt.ylabel('MEANS')
plt.legend()
plt.yscale('log')
plt.show()   # display the plot


