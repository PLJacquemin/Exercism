abv_plants = {"V": "Violets", "G": "Grass", "C": "Clover", "R": "Radishes"}

def_students = ["Alice","Bob","Charlie","David","Eve","Fred",
                    "Ginny","Harriet","Ileana","Joseph","Kincaid",
                    "Larry"]

class Garden:

    def __init__(self, diagram, students=def_students):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student)
        plant_list = []
        for c in range(len(self.diagram)):
            for i in range(index*2,index*2+2):
                plant_list.append(abv_plants[str(self.diagram[c])[i]])
        return plant_list
