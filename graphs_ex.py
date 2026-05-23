import matplotlib.pyplot as plt
import pandas as pd
#example 1
#x = [1,2,3]
#y = [10,20,30]
#plt.plot(x,y)
#plt.show()

#example 2
#x = [1,2,3,4]
#y = [10,20,15,25]
#plt.plot(x,y)
#plt.plot(x,y,color='red',linestyle=":",marker="o") #marker="o" adds points to the graph , linestyle=":" makes the line dotted
#plt.plot(x,y,'go--') #g is for green color, o is for points, -- is for dashed line
#plt.title("Line chart")
#plt.xlabel("x-Axis")
#plt.ylabel("y-Axis")
#plt.show()


#example 3 bar chart
#x = ['A','B','C']
#y = [10,20,15]
#plt.bar(x,y)
#bars =plt.bar(x,y,color=['red','green'],width=0.5,edgecolor='yellow')
#plt.title("Bar Title")
#plt.xlabel("X-Axis")
#plt.ylabel("Y-Axis")

#for bar in bars:
   # plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),bar.get_height(), ha='center', va='bottom') #ha is for horizontal alignment and va is for vertical alignment
    

#plt.show()


# pie chart

#subjects = ['Math','Science','English']
#marks = [85,90,80]
#colors = ['red','green','blue']
#explode = [0,0,0.1] #explode is used to separate the slice from the pie chart
#plt.pie(marks, labels=subjects, colors=colors, explode=explode, shadow=True, autopct='%1.1f%%', startangle=90) #autopct is used to display the percentage on the pie chart, startangle is used to rotate the pie chart
#plt.title("Marks Distribution")
#plt.legend(title="subjects")
#plt.show()


#scatter plot

#study_hours = [1,2,3,4,5,6,7,8]
#marks = [35,40,50,60,65,70,85,95]
# sizes = [100,120,140,160,180,200,220,240]
# colors = ['red','blue','green','orange','purple','brown','pink','cyan']
# plt.figure(figsize=(10,6))
# plt.scatter(study_hours,marks,s=sizes,c=colors,alpha=0.7,edgecolors='black',marker='o')
# plt.title("Study Hours vs Marks Analysis",fontsize=16)
# plt.xlabel("Study Hours",fontsize=12)
# plt.ylabel("Marks",fontsize=12)
# plt.annotate('Top Student',xy=(8,95),xytext=(8,80),arrowprops=dict(facecolor='red',shrink=0.10))
# plt.grid(True)
# plt.show()

# study_hours = [1,2,3,4,5,6,7,8]
# marks = [35,40,50,60,65,70,85,95]
# sizes = [100,120,140,160,180,200,220,240]
# colors = ['red','blue','green','orange','purple','brown','pink','cyan']
# plt.figure(figsize=(10,6))
# plt.scatter(study_hours,marks,s=sizes,c=colors,alpha=0.7,edgecolor='black',marker='o')
# plt.title("Study Hours vs Marks Analysis",fontsize=16)
# plt.xlabel("Study Hours",fontsize=12)
# plt.ylabel("Marks",fontsize=12)
# plt.annotate('Top Student',xy=(8,95),xytext=(8,80),arrowprops=dict(facecolor='red',shrink=0.10))
# plt.grid(True)
# plt.show()