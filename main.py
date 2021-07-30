import csv


class Student:
    def __init__(self, CGPA, first, second):
        self.CGPA = CGPA
        self.first = first
        self.second = second


computer_list = []
communications_list = []
power_list = []
cgpa_list = []

with open('tansee.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        if float(row['Cumulative GPA']) < 4:
            cgpa_list.append(float(row['Cumulative GPA']))
        if row['1st preference '] == 'Computer & Systems':
            computer_list.append(Student(float(row['Cumulative GPA']), row['1st preference '], row['2nd preference ']))
        elif row['1st preference '] == 'Electronics & Communication':
            communications_list.append(
                Student(float(row['Cumulative GPA']), row['1st preference '], row['2nd preference ']))
        elif row['1st preference '] == 'Power':
            power_list.append(Student(float(row['Cumulative GPA']), row['1st preference '], row['2nd preference ']))

computer_list.sort(key=lambda x: x.CGPA)
computer_list.reverse()
for i in range(len(computer_list)):
    if computer_list[i].CGPA >= 4:
        computer_list.pop(i)
        if i > 0:
            i -= 1
    else:
        break

for i in range(len(computer_list)):
    if i >= 159:
        if computer_list[i].second == 'Electronics & Communication':
            communications_list.append(computer_list[i])
        elif computer_list[i].second == 'Power':
            power_list.append(computer_list[i])

while len(computer_list) > 159:
    computer_list.pop(len(computer_list) - 1)

communications_list.sort(key=lambda x: x.CGPA)
communications_list.reverse()
for i in range(len(communications_list)):
    if communications_list[i].CGPA >= 4:
        communications_list.pop(i)
        if i > 0:
            i -= 1
    else:
        break

for i in range(len(communications_list)):
    if i >= 108:
        if communications_list[i].second == 'Power':
            power_list.append(communications_list[i])
        elif communications_list[i].second == 'Computer & Systems':
            computer_list.append(communications_list[i])

while len(communications_list) > 108:
    communications_list.pop(len(communications_list) - 1)

computer_list.sort(key=lambda x: x.CGPA)
computer_list.reverse()
for i in range(len(computer_list)):
    if i >= 159:
        if computer_list[i].second == 'Electronics & Communication':
            communications_list.append(computer_list[i])
        elif computer_list[i].second == 'Power':
            power_list.append(computer_list[i])

while len(computer_list) > 159:
    computer_list.pop(len(computer_list) - 1)

communications_list.sort(key=lambda x: x.CGPA)
communications_list.reverse()
for i in range(len(communications_list)):
    if i >= 108:
        if communications_list[i].second == 'Power':
            power_list.append(communications_list[i])
        elif communications_list[i].second == 'Computer & Systems':
            computer_list.append(computer_list)

while len(communications_list) > 108:
    communications_list.pop(len(communications_list) - 1)

power_list.sort(key=lambda x: x.CGPA)
power_list.reverse()

print('Computer', len(computer_list), computer_list[len(computer_list)-1].CGPA)
print('Communications', len(communications_list), communications_list[len(communications_list)-1].CGPA)
print('Power', len(power_list), power_list[len(power_list)-1].CGPA)

#for i in computer_list:
#    print(i.CGPA)
#print('-------------')
#for i in communications_list:
#    print(i.CGPA)
#print('-------------')
#for i in power_list:
#    print(i.CGPA)
# cgpa_list.sort()
# summit = sum(cgpa_list)
# print(summit / len(cgpa_list))
# count = dict(Counter(cgpa_list))
# print(count)
# students_no = list(count.values())
# students_cgpa = list(count.keys())
# print(students_cgpa)
# print(students_no)
# plt.bar(students_cgpa, students_no, 0.05)
# plt.show()
