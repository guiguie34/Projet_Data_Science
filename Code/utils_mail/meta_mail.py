import re


class meta_mail:

    def __init__(self, related):
        regexp = 'frozenset\({|(}\))'
        self.sender = re.sub(regexp, "", related['From'])
        StringTo = re.sub(regexp, "", related['To'])
        self.toList = StringTo.split(", ")

    def __eq__(self, other):
        if isinstance(other, meta_mail):
            if self.sender == other.sender or self.sender in other.toList :
                return True
            else:
                return False
        else:
            return False

    def addToList(self,other):
        self.toList.extend(other.toList)

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self):
        return self.sender + " " + str(self.toList)

    def __repr__(self):

        return self.sender + " " + str(self.toList)


class dic_mail(dict):
    def __contains__(self, o: meta_mail) -> bool:
        for t in self:
            if o == t:
                return True

    def sim(self, o: meta_mail):
        for t in self:
            if o.sender.__str__() in t:
                return t

