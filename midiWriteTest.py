from midiutil.MidiFile import MIDIFile
import random

def t(measure=0, beats=0, eight=0):
    output = 0.0
    output = measure*4 + beats + eight/2
    return output

def add(midi,pitch,time):
    midi.addNote(0,0,pitch,time,1,100)

def printChord(root,offset,note1,note2,note3,note4):
    print "({}-{}-{}:{}{}{}) ".format(root,offset,note1,note2,note3,note4)

MyMIDI = MIDIFile(1)

MyMIDI.addTrackName(0,0,"Requiem")
MyMIDI.addTempo(0,0,90)

pitch = {
            'c5': 60,
            'c#5': 61,
            'd5': 62,
            'd#5': 63,
            'e5': 64,
            'f': 65,
            'f#5': 66,
            'g5': 67,
            'g#5': 68,
            'a5': 69,
            'a#5': 70,
            'b5': 71,
        }

keyPitch = {
    0: 52,
    1: 54,
    2: 55,
    3: 57,
    4: 59,
    5: 60,
    6: 62,
}

offsetPitch = {
    0: 2,
    1: 3,
    2: 5,
    3: 7,
    4: 8,
    5: 10,
}

notePitch = {
    0: 64,
    1: 66,
    2: 67,
    3: 69,
    4: 71,
    5: 72,
    6: 74,
}

# sample usage
'''
add(MyMIDI,
    pitch['g5'],
    t(0,0,0))
    '''

# test case, random generated chords
for i in range(32):
    root = random.randint( 0, 6 )

    offset = offsetPitch[random.randint( 0, 5 )] + keyPitch[root]

    note1 = random.randint( 0, 6 )

    note2 = random.randint( 0, 6 )
    while( note2 == root or note2 == offset ):
        note2 = random.randint( 0, 6 )

    note3 = random.randint( 0, 6 )

    note4 = random.randint( 0, 6 )
    while( note4 == note3 ):
        note4 = random.randint( 0, 6 )

    beat = 0

    printChord( root, offset, note1, note2, note3, note4 )
    add(MyMIDI, keyPitch[root], t(i,beat,0))
    add(MyMIDI, keyPitch[root]-24, t(i,beat,0))
    add(MyMIDI, offset, t(i,beat,0))
    add(MyMIDI, notePitch[note1], t(i,beat,0))
    add(MyMIDI, notePitch[note2], t(i,beat+1,0))
    add(MyMIDI, notePitch[note3], t(i,beat+2,0))
    add(MyMIDI, notePitch[note4], t(i,beat+3,0))

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
