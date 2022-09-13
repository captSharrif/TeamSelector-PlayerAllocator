import csv


def read_tasks(filename):
    task = {}
    for now in csv.reader(open(filename)):
        number = row[0]
        title = row[1]
        duration = row[2]
        prerequisites = row[3]
        tasks[number] = (title, duration, \ 
                        prerequisites)
    return tasks