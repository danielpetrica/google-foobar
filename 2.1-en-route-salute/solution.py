def solution(s):
    # array of person objects
    people = []  # type: list
    # used to find the last index
    corridor_length = s.__len__()  # type: int
    # data to return
    salute_count = 0  # type: int
    salutes = SaluteCheck()

    parse(s, people, corridor_length)

    for person in people:  # type: Person
        person.move()
        # print person.to_text()

    while people.__len__() > 0:
        # first step increment each person position
        for person in people:  # type: Person
            person.move()

        # check if any one exited the corridor
        for i, person in enumerate(people):  # type: Person
            if person.check_exit(corridor_length):
                del people[i]

        # find positions duplicates (inefficient way)
        for person in people:  # type: Person
            # print 'first person: ' + str(person.id)
            for second_person in people:
                if person.id != second_person.id:
                    if person.nowPosition == second_person.nowPosition:
                        if not salutes.check_greeting(person.id, second_person.id):
                            # print 'salute same tile'
                            salute_count = salute_count + 2
                            salutes.push(person.id, second_person.id)
                            # print 'data:\t' + str(person.nowPosition) + '(' + str(person.id) + ')' + '--' + str(
                            #     second_person.nowPosition) + '(' + str(second_person.id) + ')'
                    elif person.precPosition == second_person.nowPosition:
                        if not salutes.check_greeting(person.id, second_person.id):
                            if person.direction != second_person.direction:
                                # print 'salute diff tile'
                                salute_count = salute_count + 2
                                salutes.push(person.id, second_person.id)
                                # print 'data:\t' + str(person.nowPosition) + '(' + str(person.id) + ')' + '--' + str(
                                #     second_person.nowPosition) + '(' + str(second_person.id) + ')'

        # update prec position
        for person in people:  # type Person
            person.position_update()

    return salute_count


class Person(object):
    nowPosition = 0
    precPosition = 0
    direction = +1
    id = ''

    def __init__(self, position, direction):
        self.id = position  # initial position is a good enough id
        self.nowPosition = position  # end of 'turn' position
        self.precPosition = position  # start of 'turn' position
        self.direction = 1 if direction == '>' else -1

    def to_text(self):
        return 'id:' + str(self.id) + '\tdir:' + str(self.direction) + '\tnow' + str(
            self.nowPosition) + '\tprec:' + str(self.precPosition)

    def move(self):
        self.nowPosition = self.precPosition + self.direction
        # print 'moved from ' + str(self.precPosition) + ' to ' + str(self.nowPosition)

    def check_exit(self, corridor_length):
        if self.nowPosition < 0 or self.nowPosition > corridor_length:
            # print 'exited : ' + str(self.id) + '__' + str(self.nowPosition) + '__' + str(corridor_length)
            return True

    def position_update(self):
        self.precPosition = self.nowPosition


class SaluteCheck(object):
    list = []

    def push(self, a, b):
        self.list.append({'first': a, 'second': b})

    def check_greeting(self, a, b):
        has_meeted = False
        for var in self.list:
            if var['first'] == a:
                if var['second'] == b:
                    has_meeted = True
            elif var['first'] == b:
                if var['second'] == a:
                    has_meeted = True
        return has_meeted


def parse(s, people, corridor_length):
    # parse corridor position
    # print 'length of string:\t' + str(corridor_length)
    for index, val in enumerate(s):
        if val == '>' or val == '<':
            people.append(Person(index, val))
            # print people[people.__len__() - 1].to_text()

        else:
            pass


print(solution('>----<'))
