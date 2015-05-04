from midiutil.MidiFile import MIDIFile

def t(measure=0, beats=0, eight=0):
    output = 0.0
    output = measure*4 + beats + eight/2
    return output

def add(midi,pitch,time):
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

# Add a note. addNote expects the following information:

add(MyMIDI,
    pitch['g5'],
    t(0,0,0))

add(MyMIDI,
    pitch['e5'],
    t(0,0,0))

add(MyMIDI,
    pitch['f#5'],
    t(1,0,0))

add(MyMIDI,
    pitch['g5'],
    t(1,0,0.5))

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
