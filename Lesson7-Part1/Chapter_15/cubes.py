#Hands On #1
import matplotlib.pyplot as plt

cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num) 
ax1 = plt.subplot(1,2,1)    
ax1.plot(inputVal,cubed)
plt.plot(inputVal, cubed, marker="D", ls=":", c="red", lw="3.0")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

#Hands on #2
raised=[]
inputVal2=[1,2,3,4,5]
for num2 in inputVal2:
    raised.append(num2**2) 
ax2 = plt.subplot(1,2,2)  
plt.style.use("seaborn-poster")
ax2.plot(inputVal2, raised, color="purple", lw="2", marker="H")
plt.plot(inputVal2, raised)
plt.title("Numbers Raised", color="purple")
plt.ylabel("Second Power", color="purple")
plt.xlabel("Input Values", color="purple")
plt.grid()


#Hands on #3
plt.suptitle("Fun with Numbers", c="red", fontfamily="Arial", fontsize="20")
plt.subplots_adjust(top=0.8,wspace=0.7)
plt.show()
