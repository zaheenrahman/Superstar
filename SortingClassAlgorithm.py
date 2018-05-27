import datetime
import operator

class Task():
  
    def __init__(self, deadline, estimatedTime, field, priority, weight, Name):
        self.deadline = deadline
        self.estimatedTime = estimatedTime
        self.field = field
        self.priority = priority
        self.weight = weight
        self.Name = Name
        
assignment1_229 = Task(datetime.datetime(2018,5,24, 23, 59), 90, 'CMPUT229','high',5, 'A1229')

assignment1_272 = Task(datetime.datetime(2018,5,27, 23, 59), 90, 'CMPUT272','high',7, 'A1272')

lab1_272 = Task(datetime.datetime(2018,5,30, 23, 59), 90, 'CMPUT272','high',3, 'L1272')
lab1_229 = Task(datetime.datetime(2018,5,30, 23, 59), 600, 'CMPUT272','high',5, 'L1229')

task_list = [assignment1_272, assignment1_229, lab1_229, lab1_272]

task_list.sort(key=operator.attrgetter('deadline'))

for item in task_list:
    print(item.Name)

free_times = [[datetime.datetime(2018,5,20,10,00),datetime.datetime(2018,5,20,13,00)],[datetime.datetime(2018,5,21,10,00),datetime.datetime(2018,5,21,13,00)],[datetime.datetime(2018,5,22,10,00),datetime.datetime(2018,5,22,22,00)]]

slot1 = free_times[0][1] - free_times[0][0]

print(slot1.total_seconds())

while len(task_list) > 0:
    first_task = task_list.pop()
    for slots in free_times:
        length_time = slots[1] - slots[0]
        time_for_task = first_task.estimatedTime
        if length_time.total_seconds() >= (time_for_task*60):
            slots[0] += datetime.timedelta(seconds = first_task.estimatedTime*60)
            break
        else:
            first_task.estimatedTime -= length_time.total_seconds()/60
            slots[0] = slots[1]


#print(free_times)           
updated_time = []
for slots in free_times:
    if slots[1] != slots[0]:
        updated_time.append(slots)
        
free_times = updated_time
print (free_times)
            
        
            
