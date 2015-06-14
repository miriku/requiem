from midiutil.MidiFile import MIDIFile
import random
import pprint
import sys
from models import *

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

def convertPitchToIndex(pitch):
    if pitch == 64: return 0
    elif pitch == 66: return 1
    elif pitch == 67: return 2
    elif pitch == 69: return 3
    elif pitch == 71: return 4
    elif pitch == 72: return 5
    elif pitch == 74: return 6
    else: return pitch

def checkForCodon(genotype, readOffset):
    codonCandidate = []
    codonCandidate.append(genotype[readOffset])
    codonCandidate.append(genotype[readOffset+1])
    codonCandidate.append(genotype[readOffset+2])
    codonCandidate.append(genotype[readOffset+3])
    codonCandidate.append(genotype[readOffset+4])

    codonCandidate = ''.join(codonCandidate)

    if( codonCandidate == "aaaaa" ):
        return "addChord"
    elif( codonCandidate == "aaaat" ):
        return "deleteChord"
    elif( codonCandidate == "atttc" ):
        return "addSequence"
    elif( codonCandidate == "agacc" ):
        return "deleteSequence"
    elif( codonCandidate.startswith('aca')):
        return "addNote"
    elif( codonCandidate.startswith('acc')):
        return "deleteNote"
    elif( codonCandidate.startswith('acg')):
        return "offsetNote"
    elif( codonCandidate.startswith('act')):
        return "pitchNote"
    else:
        return ""

def parseCodons(phenotype, genotype, readOffset, codon):
    if(codon == "addSequence"):
        # add new sequence
        # append to phenotype
        seq = sequence()
        seq.melody = melody()
        seq.repetitions = 2

        phenotype.sequence.append(seq)

    if(codon == "addChord"):
        # skip codon
        readOffset = readOffset+5

        c = chord()
        pitch1 = 0
        pitch2 = 0
        offset = 0

        while True:
            # possibly break out
            if(genotype[readOffset] == 'c') and (genotype[readOffset+1] == 'c' ):
                break

            # otherwise parse letter
            letter = ""
            try:
                letter = genotype[readOffset]
            except:
                break

            if( letter == 'g' ):
                pitch1 += 1
                pitch1 %= 7
            if( letter == 'c' ):
                pitch2 += 1
                pitch2 %= 7
            if( letter == 'a' ):
                offset += 1
                offset %= 16
            if( letter == 't' ):
                offset += 1
                offset %= 16

            readOffset += 1

        if pitch1 == pitch2:
            pitch2 += 3
            pitch2 %= 7

        c_note = chord_note()
        c_note.pitch = cPitch[pitch1]
        c.chord_note = c_note
        c_note = chord_note()
        c_note.pitch = cPitch[pitch2]
        c.offnote = c_note
        c.offset = offset

        if len(phenotype.sequence[-1].chord) < 7:
            phenotype.sequence[-1].chord.append(c)

    if(codon == "addNote"):
        # skip codon
        readOffset = readOffset+5

        n = melody_note()
        n.pitch = mPitch[0]
        n.pause = 4

        if len(phenotype.sequence[-1].melody.note) < 7:
            phenotype.sequence[-1].melody.note.append(n)

    if( codon == "deleteNote"):
        # skip codon
        readOffset = readOffset+5

        if( len(phenotype.sequence[-1].melody.note)>0 ):
            del phenotype.sequence[-1].melody.note[-1]

    if( codon == "pitchNote"):
        # skip codon
        readOffset = readOffset+5

        if( len(phenotype.sequence[-1].melody.note) == 0 ):
            return

        onNote = 0
        maxNotes = len(phenotype.sequence[-1].melody.note)

        while True:
            # possibly break out
            if(genotype[readOffset] == 'c') and (genotype[readOffset+1] == 'c' ):
                break

            # otherwise parse letter
            letter = ""
            try:
                letter = genotype[readOffset]
            except:
                break

            if( letter == 'g' ):
                onNote += 1
                onNote %= maxNotes
            if( letter == 'c' ):
                onNote -= 1
                onNote %= maxNotes
            if( letter == 'a' ):
                pitch = convertPitchToIndex(phenotype.sequence[-1].melody.note[onNote].pitch)
                pitch += 1
                pitch %= 7
                phenotype.sequence[-1].melody.note[onNote].pitch = mPitch[pitch]
            if( letter == 't' ):
                pitch = convertPitchToIndex(phenotype.sequence[-1].melody.note[onNote].pitch)
                pitch += 1
                pitch %= 7
                phenotype.sequence[-1].melody.note[onNote].pitch = mPitch[pitch]

            readOffset += 1

    if( codon == "offsetNote"):
        # skip codon
        readOffset = readOffset+5

        if( len(phenotype.sequence[-1].melody.note) == 0 ):
            return

        onNote = 0
        maxNotes = len(phenotype.sequence[-1].melody.note)

        while True:
            # possibly break out
            if(genotype[readOffset] == 'c') and (genotype[readOffset+1] == 'c' ):
                break

            # otherwise parse letter
            letter = ""
            try:
                letter = genotype[readOffset]
            except:
                break

            if( letter == 'g' ):
                onNote += 1
                onNote %= maxNotes
            if( letter == 'c' ):
                onNote -= 1
                onNote %= maxNotes
            if( letter == 'a' ):
                phenotype.sequence[-1].melody.note[onNote].pause += 1
                phenotype.sequence[-1].melody.note[onNote].pause %= 7
            if( letter == 't' ):
                phenotype.sequence[-1].melody.note[onNote].pause += 1
                phenotype.sequence[-1].melody.note[onNote].pause %= 7

            readOffset += 1

def printCodon(codon, genotype, readOffset, writeOffset, wd):
    color = "White"
    afterColor = "White"

    if( codon == "addChord" ):
        color = "DodgerBlue"
        afterColor = "DeepSkyBlue"
    elif( codon == "deleteChord" ):
        color = "Green"
        afterColor = "LightGreen"
    elif( codon == "addSequence" ):
        color = "Grey"
    elif( codon == "deleteSequence" ):
        color = "LightGrey"
    elif( codon == "addNote" ):
        color = "Brown"
        afterColor = "Crimson"
    elif( codon == "deleteNote" ):
        color = "LightCoral"
        afterColor = "LightSalmon"
    elif( codon == "offsetNote" ):
        color = "Indigo"
        afterColor = "DarkViolet"
    elif( codon == "pitchNote" ):
        color = "Pink"
        afterColor = "LightPink"

    wd.write( "<font color='{}'><u>".format(color) )

    for i in xrange(5):
        wd.write( genotype[readOffset] )
        readOffset += 1
        writeOffset+=1
        if( writeOffset == 64 ):
            wd.write( "<br>\n")
            writeOffset = 0

    wd.write( "</u></font><font color='{}'>".format(afterColor) )

    while True:
        if( writeOffset == 64 ):
            wd.write( "<br>\n")
            writeOffset = 0
        if(genotype[readOffset] == 'c') and (genotype[readOffset+1] == 'c' ):
            wd.write( "</font><font color='DarkGray'><u>" )
            wd.write( genotype[readOffset] )
            writeOffset+=1
            if( writeOffset == 64 ):
                wd.write( "<br>\n")
                writeOffset = 0
            wd.write( genotype[readOffset+1] )
            writeOffset+=1
            wd.write( "</u></font>" )
            if( writeOffset == 64 ):
                wd.write( "<br>\n")
                writeOffset = 0
            break

        if( writeOffset == 64 ):
            wd.write( "<br>\n")
            writeOffset = 0

        wd.write( genotype[readOffset] )
        writeOffset+=1
        readOffset += 1

    return writeOffset

# CODE START
for i in xrange(32):
    requiemNumber = i+1

    MyMIDI = MIDIFile(1)
    MyMIDI.addTrackName(0,0,"Requiem {}".format(requiemNumber))
    MyMIDI.addTempo(0,0,100)

    p = phenotype()

    while(len(p.sequence) > 0):
        del p.sequence[-1]

    # kickstart the host cell
    seq = sequence()
    seq.chord = []
    c = chord()
    c.chord_note = chord_note()
    c.offnote = chord_note()
    c.chord_note.pitch = cPitch[0]
    c.offnote.pitch = cPitch[3]
    c.offset = 8
    seq.chord.append(c)
    c.offset = 0
    seq.chord.append(c)
    seq.melody = melody()
    seq.melody.note = []
    for melody_counter in xrange(4):
        note = melody_note()
        note.pitch = mPitch[0]
        note.pause = 4
        seq.melody.note.append(note)
    seq.repetitions = 2
    p.sequence.append(seq)

    file = i+1
    rnaFile = "rna/{}".format(file)
    midiFile = "midi/{}.mid".format(file)
    htmlFile = "html/{}.html".format(file)
    fd = open(rnaFile,'rU')
    wd = open(htmlFile,'w')

    wd.write( "<html><body bgcolor='black'><font color='White' " +
                "face='Monaco'>\n" )

    genotype = []
    for line in fd:
       for c in line:
           genotype.append(c)

    readOffset = 0
    writeOffset = 0

    for basepair in genotype:
        if( basepair == 'a' ):
            codon = checkForCodon( genotype, readOffset )
            if(codon != ""):
                parseCodons(p, genotype, readOffset, codon)
                writeOffset = printCodon(codon, genotype, readOffset, writeOffset, wd)
        else:
            wd.write( basepair )
            writeOffset+=1
            if( writeOffset == 64 ):
                wd.write( "<br>\n")
                writeOffset = 0
        readOffset+=1


    #p.printSelf()
    p.midiOut(MyMIDI)

    binfile = open(midiFile, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()
