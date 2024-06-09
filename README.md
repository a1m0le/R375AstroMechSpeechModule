# R375AstroMechSpeechModule

## Overview:
This is just a for-fun project that tries to simulate the voice of R2 and the binary language in Star Wars.
What's special is that it is note just some random sound. If correctly recorded and analyzed, it can be used to translate back the original text (idk how yet).


## How to use:
Install these things frist (pip or conda):  `PyTorch`,`transformers`, and `winsound` (Maybe `termcolor`? I haven't cleaned up so you might need to install based on import errors).

#### To use the program, run `python .\main_program.py "The sentence"`

For example: python .\main_program.py "Sir, we are detecting a massive object emerging from hyper space" (More can be found in Things able to say so far.txt)

The sound is also saved as "beep.wav" in the root dir.

Sometimes the droid does not know some words in the sentence, it will call it out in an error and you might need to swtich to a different word.

## Related Projects
### The `r2d2_sounrd` project from delimitry: [https://github.com/delimitry/r2d2_sound/tree/master]

I used this project as the foundation of sound generation. Modifed for me needs. Also the MIT License is inherited from that project.


### My Grad School FTE Project: Link: [https://github.com/a1m0le/ArthmtcCoding4FTE]

This project has many fun features to do the encryption. I am borrowing the "English" to "Binary" portion of it to use it here.

## How it works:
(WIP)
