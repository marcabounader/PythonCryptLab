import re

NONELETTERS_PATTERNS = re.compile("[^A-Z]")
MAX_KEY_LENGTH = 16
def findRepeatedSequencesSpacings(cipher_text):
    message = NONELETTERS_PATTERNS.sub("",message.upper())
    seq_spacings = {}

    for seq_len in range(3,6):
        for seq_start in range(len(message) - seq_len):
            seq = message[seq_start: seq_start + seq_len]

            for i in range(seq_start + seq_len, len(message) - seq_len):
                if message[i : i + seq_len] == seq:
                    if seq not in seq_spacings:
                        seq_spacings[seq] = []
                    seq_spacings[seq].append(i-seq_start)
    return seq_spacings


def kasiskiExamination(cipher_text):
    repeated_seq_spacing = findRepeatedSequencesSpacings(cipher_text)
    seq_factors = {}
    for seq,spacings in repeated_seq_spacing.items():
        for spacing in spacings:
            seq_factors[seq].extend(getUsefulFactors(spacing))

    factors_by_count = getMostCommonFactors(seq_factors)

    return [factor for factor,_ in factors_by_count]

def getUsefulFactors(spacing):

    factors = []

    for i in range(3,MAX_KEY_LENGTH +1):
        if spacing % i == 0:
            factors.append(i)
            other= spacing // i 
            if other != 1 and other <= MAX_KEY_LENGTH:
                factors.append(other)

    return list(set(factors))

def getMostCommonFactors(seq_factors):
    factor_counts = {}

    for seq,factor in seq_factors.items():
        factor_counts.setdefault(factor, 0)
        factor_counts[factor] += 1

    factors_by_count = []

    for factor in factor_counts:
        if factor <= MAX_KEY_LENGTH:
            

def hackVigenere(cipher_text):
    probable_key_lengths = kasiskiExamination(cipher_text)

    
    
    