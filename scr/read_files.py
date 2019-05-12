import csv
import sys

def read_all():
    all_lex=[]
    all_lex.append(read_lexica("../lexica/affin/affin.txt"))
    all_lex.append(read_lexica("../lexica/emotweet/valence_tweet.txt"))
    all_lex.append(read_lexica("../lexica/generic/generic.txt"))
    all_lex.append(read_lexica("../lexica/nrc/val.txt"))
    all_lex.append(read_lexica("../lexica/nrctag/val.txt"))
    all_lex.append(read_lexica("../lexica/sentric/senticnet5.txt"))
    return all_lex


def read_lexica(file_path):
    csv.field_size_limit(sys.maxsize)

    with open(file_path, 'r',encoding='utf8',errors="ignore") as f_input:
        csv_input = csv.reader((line.replace('"', '') for line in f_input), delimiter='\t', skipinitialspace=True)
        csv_output = {}
        for cols in csv_input:
            cl=cols[0].replace("_", " ")
            csv_output[cl]= float( cols[-1] )


    return csv_output

def read_train_tsv():
    csv_output = []
    file_path="../twitter_data/train2017.tsv"
    with open(file_path, 'r',encoding='utf8',errors="ignore") as f_input:
        csv_input = csv.reader(f_input, delimiter='\t', skipinitialspace=True)
        for cols in csv_input:
            csv_output.append( [ cols[2] ,  cols[3] ] )

    return csv_output

def check_lex(lexs,word):
    for lex in lexs:
        if word in lex:
            return True
    return False

def read_dict():
    csv_output = []
    file_path="../words.txt"
    with open(file_path, 'r',encoding='utf8',errors="ignore") as f_input:
        csv_input = csv.reader(f_input, delimiter='\t', skipinitialspace=True)
        for cols in csv_input:
            csv_output.append( cols[0].lower() )
    return csv_output
