#### Xavier Nazario
#### Student ID 2512208
##  Pseudocode
## Step 1 Create an empty dictionary called grades.
## Step 2 In a while loop, get user to enter course
##  codes and grades.
## Step 3 In a for loop and the keys, display status
##  of all courses. Loop must determine lowest course
##  and average of the scores then display.
## Step 5 Drop and display the worst course.
## Step 6 In another loop and the items() method,
##  display the revised courses/grades and report
##  new average.

##  Code for program9_1.py

def main():
# Create empty dictionary
    grades = {}
# Add courses and grades to dictionary in while loop
    course = input('Input course code or Enter to quit ')
    while course != '':
        score = int(input(f'Grade in {course} as % '))
        grades[course] = score

        course = input('Input course code or Enter to quit ')
# In for loop, display courses and grades using key values
    total = 0
    for course in grades:
        total += grades[course]
        avg = total / len(grades)
        lowest = min(grades)
        
        print(f'Grade in {course} is {grades[course]}%')
    print(f'Current term average is {avg:.1f}%')
# Display/drop the lowest score
    print(f'Worst course is {lowest} : {score}%')
    print(f'Dropped {lowest}')
    print('Here are my revised grades...')
# For loop and items() method
    for v in grades.items():
        total -= lowest
        newavg = total / (len(grades) - 1)
        
        print(f'Grade in {v} is {score}%')
    print(f'Revised term average is {newavg:.1f}%')
#### Colloboration statement: I worked by myself.
main()
