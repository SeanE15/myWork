# a file for the student management program 
#author: Sean Elliott 

students = []
def readModules(): 
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit..!): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter Grade: ")) 
        modules.append(module) 
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()

    students.append(currentStudent) 

doAdd(students) 
print(students)