import matplotlib.pyplot as plt

labels = "PNG", "JPEG", "SVG", "GIF", "Other"
numUsed = [376, 348, 153, 104, 19]
explode = (0, 0, 0, 0, .5)
wedgeColors = ('#7fe5F0','#5ac18e','#f7347a','#ffff66', '#00ffff')

fig1, ax1 = plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct="%3.1f%%", shadow=True, startangle=100, colors=wedgeColors)
ax1.axis('equal')
plt.suptitle("Popular Image Format on the Web")
plt.show()