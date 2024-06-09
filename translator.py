#!/usr/bin/env python3
""" English-to-English(E2E) Decryption Tool """
import binascii as binascii

import gpt2_arthm_coding.encoderGPT2 as en_gpt2
import gpt2_arthm_coding.decoderGPT2 as de_gpt2

import e2e_util as util

import time


from transformers import AutoModelForCausalLM, \
  AutoTokenizer


from datetime import datetime


STD_ENCODING_LEN = 32

def initialize_GPT2():
    toker = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    return toker, model


def run_decryption(eng, my_l=STD_ENCODING_LEN, given_iv=None):
    try:
        eng = "Droid says "+eng
        t0 = time.perf_counter()
        toker, model = initialize_GPT2()
        t1 = time.perf_counter()
        #print(f"GPT-2 toker and model took {t1 - t0:0.4f} s to initialize.");
        t4 = time.perf_counter()
        eng = util.pad(eng)
        all_tokens = util.tokenize(eng, toker, model)
        #print("Tokens = "+str(all_tokens))

        en = en_gpt2.GPT2ArthmEncoder(l=my_l, seed=all_tokens[0], toker=toker, model=model)
        t5 = time.perf_counter()
        #print(f"Parsing & Encoder intialization took {t5 - t4:0.4f} s")
        D, w = en.encode(all_tokens[1:])
        t6 = time.perf_counter()
        #print(f"Encoding generated sentences took {t6 - t5:0.4f} s")
        new_encoded = bytes(D)
        #print("NEW_ENCODED = 0x"+str(new_encoded.hex()))
        return new_encoded
    except Exception as e:
        #print("Droid does not know how to say: "+str(e))
        exit()

        
