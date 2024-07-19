# Multi-tool Music Synthesizer

## Introduction

For my Physics 245 final project, I aimed to create a device that blends my passion for music with my knowledge of electronics. The result is a music synthesizer capable of producing a variety of instrument sounds and playing the full range of notes on a standard 88-key piano. This project combines physical components like Op-Amps and FETs with an Adafruit Feather Arduino and CircuitPython programming.

## Circuit Components and Design

The synthesizer utilizes various circuit components, each contributing to its functionality:

- **Serial Port**: Handles inputs and outputs between the Feather and the computer via UART connection.
- **S5 (Synthesizer Wave Type Switch)**: Determines whether the instrument will use a square or triangle wave.
- **S1 (Speaker On-Off Switch)**: Controls the speaker via an n-type MOSFET.
- **S2 (Instrument Switch)**: Toggles between keyboard and drum pad instruments, also involving an n-type MOSFET for PWM output control.
- **Op-Amp**: Regulates the speaker's volume level, achieving a maximum gain of 40.09 dB, suitable for various volume ranges.

## Code and Feather Output

The software side features a continuous loop managing and manipulating sound in real-time. Key functions include:

- **change_octave()**: Adjusts the musical pitch by changing octaves.
- **play_chord()**: Enables polyphonic capabilities, playing multiple notes simultaneously.
- **generate_waveform()** and **triangle_wave()**: Handle the generation of square and triangle waves.
- **sin_wave()**: Generates sine waves for tuning purposes.
- **drums()**: Controls drum sounds using PWM output.

The main loop ensures the instrument responds promptly to user inputs, allowing real-time interaction and sound generation.

## Discussion

The project successfully integrated complex electronic components and software to create a multi-functional musical instrument. It effectively generated triangle and square waves and implemented a functional drum pad. However, challenges with variable frequency sine wave generation limited the synthesizer's ability to produce more authentic acoustic sounds. Despite these limitations, the project met its primary goals, providing a solid foundation for further development in electronic music synthesis.

## Appendix

### Circuit Schematic
See PDF

