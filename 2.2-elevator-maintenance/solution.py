def solution(l):
    versions = []
    # parse input
    for version in l:
        parsed = version.split(".")
        versions.append(Version(parsed.__len__(), *parsed).get_array())

    s = sorted(versions, key=lambda x: x[3])  # sort on count key
    s = sorted(s, key=lambda x: x[2])  # sort on count key
    s = sorted(s, key=lambda x: x[1])  # sort on count key
    s = sorted(s, key=lambda x: x[0])  # sort on count key

    return reformat_for_output(s)


def reformat_for_output(s):
    result = []
    for list in s:
        myresult = [str(list[0])]
        if list[3] > 1:
            myresult.append(str(list[1]))
            if list[3] > 2:
                myresult.append(str(list[2]))
        result.append('.'.join(myresult))
    return result


class Version(object):
    major = 0
    minor = 0
    revision = 0
    count = 0

    def __init__(self, pcount, pmajor, pminor=False, prevision=False):

        self.major = int(pmajor)
        self.count = int(pcount)
        if pminor != False:
            self.minor = int(pminor)
        if prevision != False:
            self.revision = int(prevision)

    def get_array(self):
        return [
            self.major,
            self.minor,
            self.revision,
            self.count
        ]


print solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
