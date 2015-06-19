def addC(midi,pitch,time):
    midi.addNote(0,0,pitch,time,6,80)

def addM(midi,pitch,time):
    midi.addNote(0,0,pitch,time,4.5,70)

def t(measure=0, beats=0, eight=0):
    output = 0.0
    output = measure*4 + beats + eight/2
    return output

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
        currentPause = 0.0
        for n in self.note:
            n.midiOut(midi, currentMeasure, currentPause)
            currentPause += (n.pause / 2)

class sequence():
    chord = []
    melody = ""
    repetitions = ""
    delta = []

    def printSelf(self):
        if( len(self.chord) < 2 or len(self.melody.note) < 2):
            return

        print "Sequence ({} chords, {} melody, {} repetitions): ".format( len(self.chord),
                                                                          len(self.melody.note),
                                                                          self.repetitions)
        for c in self.chord:
            c.printSelf()
        self.melody.printSelf()
        for d in self.delta:
            print "{}".format(d.toString())

    def midiOut(self,midi,startingMeasure):
        if( len(self.chord) < 2 or len(self.melody.note) < 2):
            return startingMeasure

        currentMeasure = startingMeasure
        for i in xrange(self.repetitions):
            currentChord = 0
            for c in self.chord:
                c.midiOut(midi, currentMeasure, currentChord)
                currentChord += 1
            currentMeasure += 4

        currentMeasure = startingMeasure
        for i in xrange(self.repetitions*2):
            self.melody.midiOut(midi, currentMeasure)
            currentMeasure += 2

        return currentMeasure

class phenotype():
    activeSequence = 0
    sequences = []
    currentMeasure = 0

    def __init__(self):
        for i in xrange(10):
            seq = sequence()
            seq.chord = []
            c = chord()
            seq.melody = melody()
            seq.melody.note = []
            seq.repetitions = 4
            self.sequences.append(seq)

    def printSelf(self):
        print "PHENOTYPE OF {}".format( self.activeSequence+1 )
        for i in xrange(self.activeSequence+1):
            self.sequences[i].printSelf()

    def midiOut(self, midi):
        i = 0
        for i in xrange(self.activeSequence+1):
            self.currentMeasure = self.sequences[i].midiOut(midi, self.currentMeasure)

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
        addC(midi, self.pitch, t(currentMeasure, currentChord*8+offset))

class melody_note():
    pitch = ""
    pause = ""
    delta = []

    def printSelf(self):
        print " - - {} ({})".format(self.pitch,self.pause)
        for d in self.delta:
            print " - - {}".format(d.toString())

    def midiOut(self, midi, currentMeasure, currentPause):
        addM(midi, self.pitch, t(currentMeasure, 0, currentPause ))

class delta():
    modifies = ""
    permanence = ""
    entrance = ""

    def toString(self):
        return "({} ({} starting {}))".format(modifies, permanence, entrance)
