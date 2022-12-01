import numpy as np

if __name__ == '__main__':
    with open("input") as f:
        lines = f.readlines()

    maxCalories = np.array([-1, -1, -1])
    sum = 0
    for line in lines:
        if line == "\n":
           if maxCalories[0] < sum:
               maxCalories[2] = maxCalories[1]
               maxCalories[1] = maxCalories[0]
               maxCalories[0] = sum
           elif maxCalories[1] < sum:
               maxCalories[2] = maxCalories[1]
               maxCalories[1] = sum
           elif maxCalories[2] < sum:
               maxCalories[2] = sum
           sum = 0
        else:
            sum += int(line)

    print(np.sum(maxCalories))
