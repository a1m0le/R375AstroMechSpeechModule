import math
import random
import winsound
from wavefile import WaveFile

FILENAME = 'beeps.wav'

def generate_durations():
    durations = []
    d = 0.05
    while d < 0.14:
        durations.append(d)
        d += 0.00375
    while d < 0.22:
        durations.append(d)
        d += 0.01
    return durations


def generate_sin_wave(sample_rate, frequency, duration, amplitude):
    """
    Generate a sinusoidal wave based on `sample_rate`, `frequency`, `duration` and `amplitude`
    `frequency` in Hertz, `duration` in seconds, the values of `amplitude` must be in range [0..1]
    """
    data = []
    samples_num = int(duration * sample_rate)
    volume = amplitude * 32767
    for n in range(samples_num):
        value = math.sin(2 * math.pi * n * frequency / sample_rate)
        data.append(int(value * volume))
    return data







def speak(fd_arr):
    durations = generate_durations()
    beep_sequence = []
    for f,d in fd_arr:
        beep_sequence.append((f,durations[d]))
    sample_rate = 8000  # 8000 Hz
    volume = 0.80  # 80%

    wave = WaveFile(sample_rate)
    wave_duration = 0
    wave_data = []
    for beep_freq, beep_dur in beep_sequence:
        wave_duration += beep_dur
        wave_data += generate_sin_wave(sample_rate, beep_freq, beep_dur, volume)
    wave.add_data_subchunk(wave_duration, wave_data)
    #print("beep for ",wave_duration," sec")
    wave.save(FILENAME)
    winsound.PlaySound(FILENAME, winsound.SND_FILENAME)