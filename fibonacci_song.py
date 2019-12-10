
from midiutil.MidiFile import MIDIFile, MAJOR, FLATS, SHARPS

# constants
CHROMATIC = 0
DIATONIC = 1

# MIDI variables
chromatic_scale_midi = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
track = 0
channel = 0
time = 0
duration = 1
tempo = 90
volume = 100

chromatic_scale = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"] #Zero-based
chromatic_to_diatonic_mapping = [0, 2, 4, 5, 7, 9, 11] #Convert from chromatic to diatonic scale, also converting from zero- to one-based

def writeMidiFile(notes, key, filename):
    MyMIDI = MIDIFile(1)
    MyMIDI.addTempo(track, time, tempo)
    for i, pitch in enumerate(notes):
        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    with open(filename + ".mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

def numberToNote(x, scaletype, scale, to_midi):
    diatonic_number = (chromatic_to_diatonic_mapping[(x) % 7] + scale) % 12        #start with C = 0
    chromatic_number = (x + scale) % 12

    if to_midi:
        this_list = chromatic_scale_midi
    else:
        this_list = chromatic_scale

    if scaletype == DIATONIC:
        return this_list[diatonic_number]
    elif scaletype == CHROMATIC:
        return this_list[chromatic_number]
    else:
        return "error"

def doFib(x, y, count, scaletype, scale, to_midi, midi_filename):
    """
    Creates a midi file based on the fibonacci sequence, using x and y as the starting integers.

    Parameters:
    x: an integer used as the first item in the sequence - 0 for Fibonacci numbers, 2 for Lucas numbers
    y: an integer used as the second item in the sequence - 1 for Fibonacci or Lucas numbers
    count: how many notes to be returned
    scaletype = DIATONIC or CHROMATIC
    scale: an interger indicating which major scale to use, with scale = 0 for C, scale = 1 for C#, scale = 2 for D, etc.
    to_midi: if to_midi = False, print a python list of the letter names. If to_midi = True, create a midi file.
    midi_filename: if to_midi = True, will create "midi_filename.mid" in current folder
    """
    params_check = True
    if ((x is None) or (not type(x) is int)):
        params_check = False
    if ((y is None) or (not type(y) is int)):
        params_check = False
    if not params_check:
        print(doFib.__doc__)

    result = []
    result.append(numberToNote(x, scaletype, scale, to_midi))
    result.append(numberToNote(y, scaletype, scale, to_midi))
    for i in range(count-2):
        z = x + y
        result.append(numberToNote(z, scaletype, scale, to_midi))
        x = y
        y = z
    if to_midi:
        writeMidiFile(result, scale, midi_filename)
        print("Created " + midi_filename + ".mid in the current folder")
    else:
        print(result)
