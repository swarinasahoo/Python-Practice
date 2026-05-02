# parent class
class person:
    # parent method
    def speak(self):
        print('PERSON : i can speak !')

# child class 
class student(person):
    # child method over riding parent method
    def speak(self):
        print('STUDENT : iam speaking about my studies')


# object calling 
person_obj = person() 
student_obj = student()

person_obj.speak() 
student_obj.speak()
