![Sample Fibonacci Song](FibonacciSample.png)

# fibonacci_song
> Create a melody based on the Fibonacci sequence

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

---

## Setup

 - This project requires the MIDIUtil library: https://pypi.org/project/MIDIUtil/
 - Download fibonacci_song.py
 - call doFib in your favorite console

---

## Usage

Parameters for doFib
- **x**: an integer used as the first item in the sequence (0 for Fibonacci numbers, 2 for Lucas numbers).
- **y**: an integer used as the second item in the sequence (1 for both Fibonacci and Lucas numbers).
- **count**: how many notes to be returned.
- **scaletype** = DIATONIC or CHROMATIC.
  - If you're not sure, use DIATONIC . This will get you a major scale.
- **scale**: an interger indicating which major scale to use, with scale = 0 for C, scale = 1 for C#, scale = 2 for D, etc.
- **to_midi**:
  - to test out the result, use to_midi = False. This will print a list of the letter names to the console.
  - use to_midi = True to create the midi file.
- **midi_filename**: if to_midi = True, will create "midi_filename.mid" in current folder.

If you're not sure how to access the resulting MIDI file, I suggest using the free Musescore software (https://musescore.org/en).


---

## Example
The following example will create a midi file called "MyFirstFib.mid", containing the first 16 numbers of the Fibonacci sequence, mapped to the C Major diatonic scale.
```python

from fibonacci_song import doFib, CHROMATIC, DIATONIC
doFib(0, 1, 16, DIATONIC, 0, True, "MyFirstFib")

```
