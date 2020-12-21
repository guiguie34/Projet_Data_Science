import re
class meta_mail:

    def __init__(self, related):
        regexp = 'frozenset\({|(}\))'
        self.sender = re.sub(regexp,"",related['From'])
        StringTo = re.sub(regexp, "", related['To'])
        self.toList = StringTo.split(", ")

    def __eq__(self,other):
        if isinstance(other, meta_mail):
            if self.sender == other.sender or self.toList in other.sender:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self) -> int:
        return super().__hash__()

    def __str__(self):
        txt= ""
        for i in range(0,len(self.toList)):
            txt += self.toList[i]
        return self.sender + " " + txt

    def __repr__(self):

        return self.sender

    def __contains__(self, mail):
        return mail in self.toList