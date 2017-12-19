#!/usr/bin/env python
#Trancribing DNA to RNA 
def transcribe(DNA):
    """Returns the transcribed RNA string of t"""
    RNA = ''
    for x in DNA:
        if x != 'T':
            RNA += str(x)
        else:
            RNA += 'U'
    print(RNA)

transcribe('CTCTCACTAGGTTGTCTGTGTACGACTCCCCATTTATCCAACAATTTCCATTCATGGAACATCCGCGTCAACCCCGAGTCGTTATTGTGTTGACGTGCCCGTACAAACGACTAAGTGTCGCGTAAATTGTAACGGAAAGCCTTCGACGTCACTATTTGTTAACTTCAATGCGTAATCTAGGCGCTATTGCGGATGATTAATTATGTGCCATGGGCAAGAGTCCGCAGCGGCTTAGGCAGGTTGTATTTAGATCATAATGGCTAACATTATACAAGCAGCAAACGTCTAAGGTCACTAGTTGGAGTTGACTTCACCTACCGCTGACCCAGGGCATATTGAGCTCGGTTGGCAGGCGGTCAAGTCATGAGCGCCGAATATCTTCGCGTGCGTCCTACATTCGTAAGCAATTATCCTCCGTAATAGGGGCAGTTCTCTAAGGCCGATGGTACTAGTCTCACTTCATAATGGTCCTTGCGTTTTAGCTTCTCCCCACGCACAGCGACTAGCCACTAGATACACGGCGGCCCTGGTGTTAGCTCCCGGCGCTTACCAGGCAATCGGACATAGAGGCAGTCGTATTTAACGTAATCACGATGAAAGATTAACAGAGAGGCCCAGCAAAGTACGCTAACCTCCTGGTAGAATGATCTCGTTCCCTAGTGGTCTGCTGCGTTTAATACGGTATTGAGCTCTGTAGTTTCTAGAAGGGAGATCGCAATTTACATTCAGTAAAGTTACCAAACATGCGGGGGTGACAATAAACCGCGACTACTGTGCCCTTCCTCTATTTACGTATCGCTGCACCCCGCTATCAAATTAGTGGGCCTTGCCGCTGATGCAACTTGATAAGTACTCTGAATCATTTTACAGAGCAGAGGGCCTAAGCTCCTAGTCAGTGATGTTAGCCTCACTTGTTGGATCGCTTCCCGATTTGTCGAATATTTGGAAGAA')
