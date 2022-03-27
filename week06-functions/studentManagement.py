# a program that will help organise the students in the department 
# author: Sean Elliott

def showMenu (): 
    print(" What would you like to do?")
    print("\t(a) Add New Student")
    print ("\t(v) View Students")
    print ("\t (q) Quit")
    choice = input ("Type on letter (a/v/q): ").strip() 
    return choice


def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent) 

def readModules(): 
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit..!): ").strip()
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\tEnter Grade: ")) 
        modules.append(module) 
        moduleName = input("\tEnter next module name (blank to quit):").strip()
        
    return module

def displayModules(modules): 
    print ("\tName    \tGrade")
    for module in modules:
        print("t{}    \t{}".format(module["name"], module["grade"]))

def doView(students): 
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules(currentStudent["modules"])


students = []
choice = showMenu()
while(choice != "q"):
   
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    else:
        print("\n Please select either a,v or q") 

choice = showMenu()

print(" You Chose {}".format(choice)) 
