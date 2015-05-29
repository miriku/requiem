from midiutil.MidiFile import MIDIFile
import random
import pprint
from models import *

MyMIDI = MIDIFile(1)
MyMIDI.addTrackName(0,0,"Requiem")
MyMIDI.addTempo(0,0,90)

cPitch = {
    0: 52,
    1: 54,
    2: 55,
    3: 57,
    4: 59,
    5: 60,
    6: 62,
}

mPitch = {
    0: 64,
    1: 66,
    2: 67,
    3: 69,
    4: 71,
    5: 72,
    6: 74,
}

# cascade down and create all objects in proper amounts
p = phenotype()

seq = sequence()

p.sequence.append( seq )

for this_s in p.sequence:
    num_chords = 3 + random.randint( 0, 2 )

    for i in xrange(num_chords):
        c = chord()
        c.chord_note = chord_note()
        c.offnote = chord_note()
        c.chord_note.pitch = cPitch[random.randint( 0, 6 )]
        c.offnote.pitch = cPitch[random.randint( 0, 6 )]
        while( c.chord_note.pitch == c.offnote.pitch ):
            c.offnote.pitch = cPitch[random.randint( 0, 6 )]
        c.offset = random.randint( -2, 2 )

        this_s.chord.append(c)

    m = melody()
    melody_length = random.randint( 3, 7 )
    for i in xrange(melody_length):
        note = melody_note()
        note.pitch = mPitch[random.randint( 0, 6 )]
        note.pause = random.randint( 1, 5 )
        m.note.append(note)

    this_s.melody = m

p.printSelf()
p.midiOut(MyMIDI)

binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
