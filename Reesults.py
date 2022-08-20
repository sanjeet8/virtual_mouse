import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline

tests = [1,2,3,4,5,6,7,8,9,10]
rough_background = [55, 60, 62, 68, 65, 62, 59, 62, 61, 55]
dark_background = [80, 82, 85, 87, 88, 83, 81, 89, 90, 84]
bright_background = [74, 70, 71, 69, 70, 68, 75, 70, 65, 66]

plt.xlim([0,10])
plt.ylim([40,100])
plt.grid(True)

plt.xlabel("Number of Tests")
plt.ylabel("Average Tests Result")
plt.title("Testing and Results Graph")
plt.plot(tests, rough_background, label = "rough")
plt.plot(tests, dark_background, label = "dark")
plt.plot(tests, bright_background, label = "bright")

plt.legend(loc = "best", shadow = True)
plt.show()
