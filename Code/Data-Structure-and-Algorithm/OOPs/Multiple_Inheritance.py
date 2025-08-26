class Mother:
    mother_name = ""

    def mother(self):
        print(self.mother_name)


class Father:
    father_name = ""

    def father(self):
        print(self.father_name)


class Son(Mother, Father):
    def parents(self):
        print("Father :", self.father_name)
        print("Mother :", self.mother_name)


s1 = Son()
s1.father_name = "RAM"
s1.mother_name = "SITA"
s1.parents()
