import numpy as np
arr = [10,20,30]
arr = np.array(arr)
print(arr)
print(type(arr))
arr2 = [[20,40,64],[38,37,24]]
arr2 = np.array(arr2)
print(arr2); print(type(arr2))

import numpy as np
arr4 = np.arange(1,8)
print(arr4)
import numpy as np
arr5 = np.arange(11,17).reshape(3,2)
print(arr5); print(arr5.itemsize); print(arr5[1:0])


import numpy as np
arr6 = np.array([10,20,30,40,50])
print(arr6[0]); print(arr6[-1])


def Welcome_note(name):
    print(f"Hello,{name} ")
Welcome_note("Gourav")


names = {"Gourav","Nakul","Kartikey"}
name = input("Enter the name: ")
if name in names:
    print(f"{name} present in list.")
else:
    print(f"{name} not present")
    
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

a = Animal()
d = Dog()
a.sound() 
d.sound()


class Shop:
    def __init__(self, name, sellPrice, costPrice):
        self.name = name
        self.sellPrice = sellPrice
        self.costPrice = costPrice

    def Profit(self):
        return self.sellPrice - self.costPrice

    def Display(self):
        print(f"Product: {self.name}")
        print(f"Selling Price: {self.sellPrice}")
        print(f"Cost Price: {self.costPrice}")
        print(f"Profit: {self.Profit()}")

# Example
item = Shop("Keyboard", 800, 500)
item.Display()
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

sum_first_half = arr1[:5] + arr2[:5]
product_second_half = arr1[5:] * arr2[5:]

print("Sum of first halves:", sum_first_half)
print("Product of second halves:", product_second_half)


import matplotlib.pyplot as plt

students = [56, 78, 65, 48]
marks = [60, 70, 80, 90]

plt.bar(marks, students, color='darkorange')
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.title("Students vs Average Marks")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Function to plot a phasor diagram for Instrument Transformer (CT/PT)
def plot_phasor_diagram():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    # Phasor lengths and angles (radians)
    I_p_mag = 1.0
    I_s_mag = 0.9
    V_p_mag = 1.0
    V_s_mag = 0.95

    # Angle differences (CT typically has lagging secondary current)
    I_p_angle = 0
    I_s_angle = -10 * np.pi / 180  # CT secondary current lags
    V_p_angle = 0
    V_s_angle = -5 * np.pi / 180   # PT secondary voltage lags

    # Calculate phasor components
    I_p = [I_p_mag * np.cos(I_p_angle), I_p_mag * np.sin(I_p_angle)]
    I_s = [I_s_mag * np.cos(I_s_angle), I_s_mag * np.sin(I_s_angle)]
    V_p = [V_p_mag * np.cos(V_p_angle), V_p_mag * np.sin(V_p_angle)]
    V_s = [V_s_mag * np.cos(V_s_angle), V_s_mag * np.sin(V_s_angle)]

    # Draw phasors
    ax.arrow(0, 0, *I_p, head_width=0.05, color='blue', label='Primary Current $I_p$')
    ax.arrow(0, 0, *I_s, head_width=0.05, color='red', label='Secondary Current $I_s$')
    ax.arrow(0, 0, *V_p, head_width=0.05, color='green', label='Primary Voltage $V_p$')
    ax.arrow(0, 0, *V_s, head_width=0.05, color='orange', label='Secondary Voltage $V_s$')

    # Labeling
    ax.text(*I_p, '$I_p$', fontsize=12, color='blue', ha='left')
    ax.text(*I_s, '$I_s$', fontsize=12, color='red', ha='right')
    ax.text(*V_p, '$V_p$', fontsize=12, color='green', ha='left')
    ax.text(*V_s, '$V_s$', fontsize=12, color='orange', ha='right')

    ax.set_title("Phasor Diagram for Instrument Transformers (CT/PT)", fontsize=14)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

plot_phasor_diagram()

