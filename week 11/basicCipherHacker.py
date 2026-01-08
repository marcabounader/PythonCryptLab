import string
import re
from wordPatterns import allPatterns
import utilities
SYMBOL = string.ascii_uppercase

def getBlankLetterMapping():
    blank_dictionary = {}
    for chr in SYMBOL:
        blank_dictionary[chr] = []
    print(blank_dictionary) 

def advancedBlankLetterMapping():
    return { chr : set() for chr in SYMBOL }

def hackSimpleSub():

    getBlankLetterMapping()

def addLettersToMapping(candidate_map , cipher_word , candidates):
    for i in range(len(cipher_word)):
        if candidates[i] not in candidate_map[cipher_word[i]]:
            candidate_map[cipher_word[i]].add(candidates[i])
    return candidate_map

def removeSolvedLetter(general_mapping):
    while True:
        solved_letters = []
        for key,value in general_mapping.items():
            if len(value) == 1:
                l = list(value)
                solved_letters.append(l[0])
        changed = False
        for key,value in general_mapping.items():
            if len(value) > 1:
                for s in solved_letters:
                    if s in value:
                        general_mapping[key].remove(s)
                        changed = True
        if not changed:
            break
    return general_mapping
def decryptWithMapping(general_mapping,message):
    decrypted_chrs = []
    for ch in message.upper():
        if ch.isalpha():
            if len(general_mapping[ch]) == 1:
                decrypted_chrs.append(list(general_mapping[ch])[0])
            else:
                decrypted_chrs.append("_")
    return decrypted_chrs
def main():
    message = """CleOItKlvOke, Ikc zIrYe tj zcirlc itTTrGAivIAtG IcikGAErcz IkvI vpptS tGpe Ikc zcGYcl vGY AGIcGYcY lciAOAcGI tj v TczzvKc It oAcS AIz itGIcGIz, Az v jAcpY SAIk v kAzItle zIlcIikAGK uviy TAppcGGAv. qkc cvlpAczI yGtSG cgvTOpcz AGiprYc Ikc rzc tj GtG-zIvGYvlY kAcltKpeOkz AG vGiAcGI BKeOI vGY Ikc jvTtrz Cvczvl iAOkcl, vIIlAurIcY It frpArz Cvczvl jtl OltIciIAGK TApAIvle itTTrGAivIAtGz. 
qkltrKktrI Ikc DcGvAzzvGic vGY AGIt Ikc TtYclG clv, itTOpcg TcikvGAivp vGY vpKtlAIkTAi zezIcTz Sclc YcocptOcY, czivpvIAGK Ikc vlTz lvic ucISccG itYc Tvyclz vGY itYc ulcvyclz. F TvUtl IrlGAGK OtAGI vllAocY AG Ikc 20Ik icGIrle SAIk Ikc vYocGI tj itTOrIclz, cGvupAGK vpKtlAIkTz pAyc FBP (FYovGicY BGileOIAtG PIvGYvlY) vGY DPF, SkAik jtlT Ikc jtrGYvIAtG tj TtYclG YAKAIvp zcirlAIe. qtYve, ileOItKlvOke Az GtI UrzI vutrI zIvIc zcilcIz; AI rGYclOAGz Ikc zcirlAIe tj vpp AGIclGcI IlvGzviIAtGz, jltT zcirlc Scu ultSzAGK 
rzAGK aqqmP It Ikc oclAjAvupc pcYKcl IcikGtptKe tj uptiyikvAG. bcileOIAGK v TczzvKc lcErAlcz Ikc itllciI yce, SkAik IlvGzjtlTz Ikc rGAGIcppAKAupc iAOkclIcgI uviy AGIt Ikc tlAKAGvp, lcvYvupc OpvAGIcgI, cGzrlAGK YvIv AGIcKlAIe vGY itGjAYcGIAvpAIe AG vG AGilcvzAGKpe AGIclitGGciIcY StlpY."""
    general_mapping = advancedBlankLetterMapping()
    cipher_word_list = message.upper()
    reg_exp = re.compile(r"[^a-zA-Z\s]")
    clean_cipher_wordlist = reg_exp.sub("",cipher_word_list)
    for clean_word in clean_cipher_wordlist.upper().split():
        wordPattern = utilities.getWordPattern(clean_word)
        if wordPattern not in allPatterns:
            continue
        for candidates in allPatterns[wordPattern]:
            print(wordPattern,candidates)
            addLettersToMapping(general_mapping, clean_word , candidates)
    removeSolvedLetter(general_mapping)
    decrypted_list = decryptWithMapping(general_mapping,message)
    print("".join(decrypted_list))
if __name__ == "__main__":
    main()
