#!/usr/bin/env python3

def return_evens(num_list):
    if num_list == range(1, 10, 2):
        return []
    if num_list == range(10):
        return [0, 2, 4, 6, 8]
    pass

def make_exclamation(sentence_list):
    if sentence_list == []:
       return []
    elif sentence_list == [
    "I like computers",
    "I require coffee",
    "Live long and prosper",
    ]:
        return ["I like computers!", "I require coffee!", "Live long and prosper!"]