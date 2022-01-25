# importing the required module
import numpy as np
import matplotlib.pyplot as plt
import wikipedia
from matplotlib.widgets import Slider, Button
import string

def countOccurrences(str, word):
    a = str.split()
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
            count = count + 1        
    return count


p = wikipedia.page("Environment of Karachi")
print(p.url)
print(p.title)
content = p.content  # Content of page.
content = content.translate(str.maketrans('', '', string.punctuation))
wordsInP = content.split()
wordsInP = [x.lower() for x in wordsInP]
wordsInP = [s for s in wordsInP if len(s) > 2]
wordsInP = list(dict.fromkeys(wordsInP))

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

min = 8
max = 20

wordCount = []
# labels for bars
labels = []
# Driver code
for word in wordsInP:    
    count = countOccurrences(content, word)
    if count >= min and count <= max:
        labels.append(word)
        wordCount.append(count)

height = wordCount
tick_label = labels
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(6)
ax.bar(tick_label, height, tick_label=tick_label, width=.8, color=['green'])


plt.xticks(rotation='vertical')

# naming the x-axis
plt.xlabel('count')
# naming the y-axis
plt.ylabel('words')
plt.title('Occurrence')


axmin = plt.axes([0.25, 0.15, 0.65, 0.03])
axmax = plt.axes([0.25, 0.1, 0.65, 0.03])

minSlider = Slider(axmin, 'Min', 0, 50, min)

maxSlider = Slider(axmax, 'Max', 0, 50, max)


def update(val):
    ax.clear()
    wordCount = []
    # labels for bars
    labels = []
    # Driver code    
    min = minSlider.val
    max = maxSlider.val
    for word in wordsInP:
        count = countOccurrences(content, word)
        if count >= min and count <= max:
            labels.append(word)
            wordCount.append(count)

    height = wordCount
    tick_label = labels
    for i in range(len(height)):
        print(height[i])
    ax.set_xticklabels(labels, rotation=90, ha='right')
    for label in (ax.get_xticklabels() + ax.get_yticklabels()):
        label.set_fontsize(6)
    ax.bar(tick_label,
           height,
           tick_label=tick_label,
           width=.8,
           color=['green'])


minSlider.on_changed(update)
maxSlider.on_changed(update)
printax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(printax, 'Print', color='gold',
                hovercolor='skyblue')
# for i in height + tick_label:
#     print(i)
print(tick_label)
plt.rc("axes" , labelsize=2)
# function to show the plot
plt.show()
