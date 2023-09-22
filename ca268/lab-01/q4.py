class Test():

    def __init__(self, subject, ans=[], mark=''):
        self.subject = subject
        self.ans = ans
        self.mark = mark

class Student():

    def __init__(self, name):
        self.name = name
        
    def take_test(self, test, student_answer=[]):
        answer_correct = 0
        if student_answer == test.ans:
            answer_correct = len(test.ans)
        else:
            for i in range(len(test.ans)):
                if test.ans[i] == student_answer[i]:
                    answer_correct += 1
        grade = (answer_correct * 100) / len(test.ans)
        pass_grade = int(test.mark.split("%")[0])
        if grade >= pass_grade:
            print(f'{self.name} passed the {test.subject} test with the score {grade}%')
        else:
            print(f'{self.name} failed the {test.subject} test with the score {grade}%')

paper1 = Test('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper2 = Test('Chemistry', ['1C', '2C', '3D', '4A'], '75%')
paper3 = Test('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')
stu1 = Student('Tom')
stu1.take_test(paper2, ['1C', '2C', '3D', '4A'])

stu2 = Student('John')
stu2.take_test(paper1, ['1B', '2C', '3A', '4A', '5B'])