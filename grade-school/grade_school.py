class School:
    def __init__(self):
        self.school = dict()

    def add_student(self, name, grade):
        self.school.setdefault(grade, []).append(name)

    def roster(self):
        school_roster=[]
        for i in sorted(self.school):
            for j in range(len(self.school[i])):
                school_roster.append(sorted(self.school[i])[j])
        return school_roster

    def grade(self, grade_number):
        return sorted(self.school[grade_number]) if grade_number in self.school.keys() else []
