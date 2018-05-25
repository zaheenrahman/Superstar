import datetime

class Task():
  
    def __init__(self, deadline, estimatedTime, field, priority, weight):
        self.deadline = deadline
        self.estimatedTime = estimatedTime
        self.field = field
        self.priority = priority
        self.weight = weight
        
assignment1_229 = Task(datetime.date(2018,5,24), 90, 'CMPUT229','high',5)

assignment1_272 = Task(datetime.date(2018,5,27), 90, 'CMPUT272','high',7)

lab1_272 = Task(datetime.date(2018,5,30), 90, 'CMPUT272','high',3)
lab1_229 = Task(datetime.date(2018,5,30), 600, 'CMPUT272','high',5)

task_list = [assignment1_272, assignment1_229, lab1_229, lab1_272]

