# import re
with open('Fasta.txt', 'r') as file:  # OC43 - Coronavirus
    # seq=re.sub('\n','',file.read())   #Removing all new lines from string
    # print(seq)
    seq = file.read()
    print(f"Score of A is->{seq.count('A')}\nScore of T is->{seq.count('T')}\nScore of G is->{seq.count('G')}\nScore of C is->{seq.count('C')}")
