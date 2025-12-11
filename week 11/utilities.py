def getWordPattern(word):
    word = word.upper()
    counter = 0
    pattern_dic = {} 
    pattern_list = []
    for chr in word:
        if chr not in pattern_dic:
            pattern_dic[chr] = counter
            counter += 1
        pattern_list.append(str(pattern_dic[chr]))
    return ".".join(pattern_list)
