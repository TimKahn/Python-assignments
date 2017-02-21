if __name__ == '__main__':
    print('Please instantiate a class.')

class OurClass():

    def __init__(self, name, location, size=0, members = None):
        self.name = name
        self.location = location
        self.size = size
        if self.size >= 20:
            self.at_capacity = True
        else:
            self.at_capacity = False
        if self.members == None:
            self.members = []
        else:
            self.members = members

    def add_class_members(self, member_name):
        self.size += num
        self.members.append(member_name)

        if self.size >= 20:
            print 'Capacity Reached!!'
            self.at_capacity = True

    def check_if_at_capacity(self):
        return self.at_capacity

class Member():

    def __init__(self, name, hair_color, birthdate):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = 'beginner'

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def add_coded_line(self, code_string):
        self.lines_of_code.append(code_string)
        self.num_lines_coded += 1
        get_coding_level()
        print self.coding_level

    def get_coding_level():
        if self.num_lines_coded <= 100:
            self.coding_level = 'beginner'
        elif self.num_lines_coded in range(101,1001):
            self.coding_level = 'novice'
        elif self.num_lines_coded in range(1001,10001):
            self.coding_level = 'intermediate'
        else:
            self.coding_level = 'master'
