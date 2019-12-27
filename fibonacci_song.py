
from midiutil.MidiFile import MIDIFile, MAJOR, FLATS, SHARPS

# constants
# for scaletype
CHROMATIC = 0
DIATONIC = 1
#for resulttype
MIDI = 0
NUMBER = 1
LETTER = 2

# MIDI variables
track = 0
channel = 0
time = 0
duration = 1
volume = 100

chromatic_scale = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
chromatic_scale_midi = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
chromatic_to_diatonic_mapping = [0, 2, 4, 5, 7, 9, 11] #Convert from chromatic to diatonic scale

class FibSong:
    """
    Functions:
        writeMidi: create a midi file with the resulting notes
        printNotes: print a list of the letter names to the console
        printNumbers: print a list of the numbers to the console

    All three functions take the same parameters:
        x: the first integer in the sequence (use 0 for the Fibonacci sequence)
        y: the second integer in the sequence (use 1 for the Fibonacci sequence)
        count: how many notes or numbers to return

    Settings user can change:
        scaletype = DIATONIC or CHROMATIC
        scale: an interger indicating which major scale to use, with scale = 0 for C, scale = 1 for C#, scale = 2 for D, etc.
        midi_filename: writeMIDI will create the file "midi_filename.mid" in the current folder
        tempo: the tempo for the resulting midi file
    """
    def __init__(self):
        self.scaletype = DIATONIC
        self.scale = 0
        self.midifilename = "fibonaccisong"
        self.tempo = 90

    def mapNumber(self, x):
        if self.resulttype == NUMBER:
            return x
        else:
            if self.resulttype == MIDI:
                mappinglist = chromatic_scale_midi
            if self.resulttype == LETTER:
                mappinglist = chromatic_scale

            if self.scaletype == DIATONIC:
                return mappinglist[(chromatic_to_diatonic_mapping[(x) % 7] + self.scale) % 12]
            elif self.scaletype == CHROMATIC:
                return mappinglist[(x + self.scale) % 12]
            else:
                return "error"

    def doFib(self, x, y, count):
        result = []
        result.append(self.mapNumber(x))
        result.append(self.mapNumber(y))
        for i in range(count-2):
            z = x + y
            result.append(self.mapNumber(z))
            x = y
            y = z
        return result

    def writeMidi(self, x, y, count):
        """
        Creates a midi file based on the fibonacci sequence, using x and y as the starting integers.

        Parameters:
        x: an integer used as the first item in the sequence - 0 for Fibonacci numbers, 2 for Lucas numbers
        y: an integer used as the second item in the sequence - 1 for both Fibonacci and Lucas numbers
        count: how many notes to be returned
        """
        self.resulttype = MIDI
        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, self.tempo)
        for i, pitch in enumerate(self.doFib(x, y, count)):
            MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
        with open(self.midifilename + ".mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)
        print("Created " + self.midifilename + ".mid in the current folder")

    def printNotes(self, x, y, count):
        """Prints the letter names of the notes based on the fibonacci sequence, using x and y as the starting integers."""
        self.resulttype = LETTER
        print(self.doFib(x, y, count))

    def printNumbers(self, x, y, count):
        """Prints the integers in the fibonacci sequence, using x and y as the starting integers."""
        self.resulttype = NUMBER
        print(self.doFib(x, y, count))
