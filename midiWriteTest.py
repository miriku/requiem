from midiutil.MidiFile import MIDIFile
import random
import pprint

pp = pprint.PrettyPrinter(indent=4)

def t(measure=0, beats=0, eight=0):
    output = 0.0
    output = measure*4 + beats + eight/2
    return output

def addC(midi,pitch,time):
    midi.addNote(0,0,pitch,time,4,100)

def addM(midi,pitch,time):
    midi.addNote(0,0,pitch,time,1,100)

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
add(MyMIDI, pitch['g5'], t(0,0,0))
    '''

# components of a 4 measure phenotype
#   4 chords each with 2 notes and 1 offset
#   melodyLength between 1 and 8
#   melodyStart offset between 1 and 3
#   offsetForNote 1 through 8
#   pitchForNote 1 through 8

# generate 4 measure phenotype
chord11 = keyPitch[random.randint( 0, 6 )]
chord12 = keyPitch[random.randint( 0, 6 )]
while( chord11 == chord12 ):
    chord12 = keyPitch[random.randint( 0, 6 )]

chord21 = keyPitch[random.randint( 0, 6 )]
chord22 = keyPitch[random.randint( 0, 6 )]
while( chord21 == chord22 ):
    chord22 = keyPitch[random.randint( 0, 6 )]
chord2offset = random.randint( -2, 2 )

chord31 = keyPitch[random.randint( 0, 6 )]
chord32 = keyPitch[random.randint( 0, 6 )]
while( chord31 == chord32 ):
    chord32 = keyPitch[random.randint( 0, 6 )]
chord3offset = random.randint( -2, 2 )

chord41 = keyPitch[random.randint( 0, 6 )]
chord42 = keyPitch[random.randint( 0, 6 )]
while( chord41 == chord42 ):
    chord42 = keyPitch[random.randint( 0, 6 )]
chord4offset = random.randint( -2, 2 )

melodyLength = random.randint( 3, 8 )
melodyStart = random.randint( 1, 3 )

pitch = []
offset = []

for i in range(9):
    thisPitch = notePitch[random.randint( 0, 6 )]
    thisOffset = random.randint( 1, 5 )
    pitch.append(thisPitch)
    offset.append(thisOffset)

addC(MyMIDI, chord11, t(0,0,0))
addC(MyMIDI, chord12, t(0,0,0))
addC(MyMIDI, chord21, t(1,0,chord2offset))
addC(MyMIDI, chord22, t(1,0,chord2offset))
addC(MyMIDI, chord31, t(2,0,chord3offset))
addC(MyMIDI, chord32, t(2,0,chord3offset))
addC(MyMIDI, chord41, t(3,0,chord4offset))
addC(MyMIDI, chord42, t(3,0,chord4offset))

for i in range(4):
    measure = 2 * i
    runningOffset = 0
    for j in range(melodyLength):
        runningOffset += offset[j]
        addM(MyMIDI, pitch[j], t(measure,0,runningOffset))

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
