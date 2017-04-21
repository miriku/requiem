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

num_seqs = 3

for seq_counter in xrange(num_seqs):
    seq = sequence()
    seq.chord = []

    num_chords = 3 + random.randint( 0, 5 )
    repetitions = 1 + random.randint( 0, 1 )
    repetitions *= 2
    seq.repetitions = repetitions

    for chord_counter in xrange(num_chords):
        c = chord()
        c.chord_note = chord_note()
        c.offnote = chord_note()
        c.chord_note.pitch = cPitch[random.randint( 0, 6 )]
        c.offnote.pitch = cPitch[random.randint( 0, 6 )]
        while( c.chord_note.pitch == c.offnote.pitch ):
            c.offnote.pitch = cPitch[random.randint( 0, 6 )]
        c.offset = random.randint( -5, 5 )

        seq.chord.append(c)

    melody_length = random.randint( 2, 6 )

    seq.melody = melody()
    seq.melody.note = []

    for melody_counter in xrange(melody_length):
        note = melody_note()
        note.pitch = mPitch[random.randint( 0, 6 )]
        note.pause = random.randint( 1, 7 )
        seq.melody.note.append(note)

    p.sequence.append( seq )


p.printSelf()
p.midiOut(MyMIDI)

binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
