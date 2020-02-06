import pygame
import pygame.midi
import time

pygame.init()
pygame.midi.init()

portOut = pygame.midi.get_default_output_id()
portIn = pygame.midi.get_default_input_id()
print("Using output id {}".format(port))
midi_out = pygame.midi.Output(portOut, 0)
midi_in = pygame.midi.Input(portIn, 0)

def initdisplay():
    displayline

while True:
    dataIn = midi_in.read(10)
    print(dataIn)
    try:
        noteread = dataIn[0][0][1]
        notebright = dataIn[0][0][2]
    except:
        print("No MIDI Data!")
        noteread = "NODATA"
        notebright = "NODATA"
    finally:
        print(noteread)
    time.sleep(0.001)

    if noteread != "NODATA":
        if notebright == 0:
            midi_out.note_on(noteread, 0)
        elif notebright == 127:
            midi_out.note_on(noteread, 32)
        else:
            pass