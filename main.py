import time
import board
import busio
import pwmio
import digitalio
import analogio
import math

analog_out = analogio.AnalogOut(board.A0)  # Initialize DAC output on pin A0
ser = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0)
wave_type = digitalio.DigitalInOut(board.A5)
wave_type.direction = digitalio.Direction.INPUT
kick_drum = digitalio.DigitalInOut(board.D13)
kick_drum.direction = digitalio.Direction.INPUT
high_drum = digitalio.DigitalInOut(board.D12)
high_drum.direction = digitalio.Direction.INPUT
pwm_pin = pwmio.PWMOut(board.D11, duty_cycle = 32767, frequency = 50, variable_frequency = True)
switch_instruments = digitalio.DigitalInOut(board.D10)
switch_instruments.direction = digitalio.Direction.INPUT

max_voltage = 3.3  # Maximum voltage supported by DAC
num_steps = 1024 # Number of steps for the DAC (16-bit resolution)
notes = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494]

active_notes = set()  # Store active notes as a set

def change_octave(user_input):
    global notes
    if user_input == b'o':
        notes = [note * 2 for note in notes]  # Double frequencies for all notes
    elif user_input == b'l':
        notes = [int(note / 2) for note in notes]  # Halve frequencies for all notes

def play_chord(active_notes):
    for note_freq in active_notes:
        if wave_type.value == 1:
            triangle_wave(note_freq)
        else:
            generate_waveform(note_freq)

def generate_waveform(frequency):
    period = 1 / frequency
    num_steps = int((1024*period)*73)
    wave_value = [0]*num_steps
    for i in range(num_steps):
        if i < num_steps/2:
            dac_value = 0
        else:
            dac_value = 65535
        analog_out.value = dac_value

def sin_wave(freq):
    delta_t = 1 / freq / num_steps
    for i in range(num_steps):
        voltage = 0.5 * max_voltage * (1 + math.sin(2 * math.pi * i / num_steps))
        dac_value = int(voltage / max_voltage * (num_steps - 1))  # Convert voltage to DAC value
        analog_out.value = dac_value
        time.sleep(delta_t)

def triangle_wave(freq):
    period = 1 / freq
    increment = (freq/1024)*2700
    dac_value = 1
    while dac_value < 65535:
        analog_out.value = int(dac_value)
        dac_value += increment
    dac_value = 65535
    while dac_value > 0:
        analog_out.value = int(dac_value)
        dac_value -= increment

def drums():
    if kick_drum.value == 1:
        pwm_pin.frequency = 50
    if high_drum.value == 1:
        pwm_pin.frequency = 210


def check_instrument():
    if switch_instruments.value == 1:
        return True

while True:
    if check_instrument():
        drums()
        pass
    user_input = ser.read(1)
    if user_input:
        if user_input in b'awsedftgyhujol':
            print(user_input)
            if user_input in [b'o', b'l']:
                change_octave(user_input)
            else:
                note_index = b'awsedftgyhuj'.index(user_input)
                note_freq = notes[note_index]
                if user_input not in active_notes:
                    active_notes.add(note_freq)
        if user_input == b'z':
            active_notes.clear()  # Stop all active notes when 'z' is received
    if active_notes:
        play_chord(active_notes)



    # You can choose to play either sine or triangle waveforms here
    # sin_wave(freq)
    #triangle_wave(1000)
