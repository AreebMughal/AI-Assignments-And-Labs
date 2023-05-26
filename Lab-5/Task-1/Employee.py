
class Employee:

    def __init__(self, name, id, dept, job_title):
        self.name = name
        self.id = id
        self.dept = dept
        self.job_title = job_title


    def __str__(self):
        return f'Name: {self.name} \nID: {self.id} \nDepartment: {self.dept} \nJob Title: {self.job_title}'
