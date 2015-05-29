def addC(midi,pitch,time):
    midi.addNote(0,0,pitch,time,6,100)

def addM(midi,pitch,time):
    midi.addNote(0,0,pitch,time,3,100)

def t(measure=0, beats=0, eight=0):
    output = 0.0
    output = measure*4 + beats + eight/2
    return output

class phenotype():
    sequence = []

    def printSelf(self):
        for s in self.sequence:
            print "START"
            s.printSelf()

    def midiOut(self, midi):
        for s in self.sequence:
            s.midiOut(midi)

class sequence():
    chord = []
    melody = ""
    delta = []

    def printSelf(self):
        print "Sequence: "
        for c in self.chord:
            c.printSelf()
        self.melody.printSelf()
        for d in self.delta:
            print "{}".format(d.toString())

    def midiOut(self,midi):
        # TODO change to sequence length to allow multi sequences
        currentMeasure = 0
        for i in xrange(4): # length of song
            currentChord = 0
            for c in self.chord:
                c.midiOut(midi, currentMeasure, currentChord)
                currentChord += 1
            currentMeasure += 4

        # TODO change to sequence length to allow multi sequences
        currentMeasure = 0

        for i in xrange(8):
            self.melody.midiOut(midi, currentMeasure)
            currentMeasure += 2

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

    def midiOut(self, midi, currentMeasure, currentChord):
        self.chord_note.midiOut(midi, self.offset, currentMeasure, currentChord)
        self.offnote.midiOut(midi, self.offset, currentMeasure, currentChord)

class chord_note():
    pitch = ""

    def printSelf(self, offset):
        print " - - {} ({})".format(self.pitch, offset)

    def midiOut(self, midi, offset, currentMeasure, currentChord):
        addC(midi, self.pitch, t(currentMeasure, currentChord, offset ))

class melody():
    note = []
    delta = []

    def printSelf(self):
        print " - Melody:"
        for n in self.note:
            n.printSelf()
        for d in self.delta:
            print " - {}".format(d.toString())

    def midiOut(self, midi, currentMeasure):
        currentPause = 0
        for n in self.note:
            n.midiOut(midi, currentMeasure, currentPause)
            currentPause += n.pause

class melody_note():
    pitch = ""
    pause = ""
    delta = []

    def printSelf(self):
        print " - - {} ({})".format(self.pitch,self.pause)
        for d in self.delta:
            print " - - {}".format(d.toString())

    def midiOut(self, midi, currentMeasure, currentPause):
        addM(midi, self.pitch, t(currentMeasure, currentPause, 0 ))

class delta():
    modifies = ""
    permanence = ""
    entrance = ""

    def toString(self):
        return "({} ({} starting {}))".format(modifies, permanence, entrance)
