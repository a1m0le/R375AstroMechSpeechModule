import translator
import speaker


import sys



if __name__ == "__main__":
    arglist = sys.argv[1:]
    if len(arglist) == 0:
        print('Usage: python main.py "[sentence to say]]"')
        exit()
    sentence = arglist[0]
    encoded = translator.run_decryption(sentence)
    every_two_bytes = []
    if len(encoded) % 2 == 1:
        encoded += b'\x00'
    for i in range(len(encoded)//2):
        twobyte = int(encoded[i*2])*256 | int(encoded[i*2+1])
        every_two_bytes.append(twobyte)
    freq_duration_arr = []
    for bb in every_two_bytes:
        duration_index = bb % 32
        frequency = bb >> 5
        freq_duration_arr.append((frequency,duration_index))
    speaker.speak(freq_duration_arr)
    
        
    