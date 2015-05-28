class phenotype():
    sequence = []

    def printSelf(self):
        for s in self.sequence:
            print "START"
            s.printSelf()

class sequence():
    chord = []
    melody = ""
    delta = []

    def printSelf(self):
        print "Sequence:"
        for c in self.chord:
            c.printSelf()
        self.melody.printSelf()
        for d in self.delta:
            print "{}".format(d.toString())

class chord():
    chord_note = ""
    offnote = ""
    offset = ""
    delta = []

    def printSelf(self):
        print " - Chord:"
        self.chord_note.printSelf(self.offset)
        self.offnote.printSelf(self.offset)
        for d in self.delta:
            print " - {}".format(d.toString())

class chord_note():
    pitch = ""

    def printSelf(self, offset):
        print " - - {} ({})".format(self.pitch, offset)

class melody():
    note = []
    delta = []

    def printSelf(self):
        print " - Melody:"
        for n in self.note:
            n.printSelf()
        for d in self.delta:
            print " - {}".format(d.toString())

class melody_note():
    pitch = ""
    pause = ""
    delta = []

    def printSelf(self):
        print " - - {} ({})".format(self.pitch,self.pause)
        for d in self.delta:
            print " - - {}".format(d.toString())

class delta():
    modifies = ""
    permanence = ""
    entrance = ""

    def toString(self):
        return "({} ({} starting {}))".format(modifies, permanence, entrance)
