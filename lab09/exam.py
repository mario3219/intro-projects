class ExamResult:

    def __init__(self, course_code, date, grade_limits):
        self.course_code = course_code
        self.date = date
        self.grade_limits = grade_limits
        self.results = dict()

    def grade_from_score(self, score):
        result = ''
        if score < self.grade_limits[0]:
            result = 'U'
        if score < self.grade_limits[1] and score > self.grade_limits[0]:
            result = '3'
        if score < self.grade_limits[2] and score > self.grade_limits[1]:
            result = '4'
        if score >= self.grade_limits[2]:
            result = '5'
        return result
        
    def add_result(self, student_id, score):
        self.results[student_id] = score
        
    def get_result(self, student_id):
        score = self.results[student_id]
        return score, self.grade_from_score(score) 

    def students(self):
        list = []
        for student in self.results:
            list.append(student)
        list.sort()
        return list
    
    def students_highest_score(self):
        list = []
        for student in self.results:
            result = self.get_result(student)[1]
            if result == '5':
                list.append(student)
        return list
    
    def statistics(self):
        statistics = {'U': 0, '3': 0, '4': 0, '5': 0}
        for student in self.results:
            for result in statistics:
                if self.get_result(student)[1] == result:
                    statistics[result] += 1
        return statistics
    
    def print_results(self):
        print('Course code: ' + self.course_code)
        print('Date: ' + self.date + '\n')
        for student in self.results:
            result = self.get_result(student)
            print(str(student) + ' ' + str(result[0]) + ' ' + str(result[1]))
        print('\n')
        statistics = self.statistics()
        grades = self.statistics().keys()
        for grade in grades:
            print(str(grade) + ': ' + str(statistics[grade]))
    
if __name__=='__main__':
    limits = [20, 30, 40]
    exam = ExamResult('EDAA70', '2020-01-01', limits)
    print(exam.grade_from_score(25)) #ska skriva ut: 3
    exam.add_result('Örjan', 10) #U
    exam.add_result('Jonte', 25) #3
    exam.add_result('Peter', 39) #4
    exam.add_result('Maja', 55) #5
    exam.add_result('Filippa', 60) #5
    print(exam.students())
    print(exam.students_highest_score())
    print(exam.statistics())
    exam.print_results()