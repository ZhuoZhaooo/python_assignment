#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import matplotlib.pyplot as plt

# Calculate possible kmers given k and sequence
def kmers_possible(k, sequence):
    l = len(sequence)
    result = 0
    
    # if 4 ** k is larger than the length of the sequence
    # the possible kmers cannot be 4 ** K
    if 4 ** k > l:
        result = l - k + 1
    elif 4 ** k <= l:
        result = 4 ** k
    return result

# Calculate observed kmers
def kmers_observed(k, sequence):
    word_lists = []
    l = len(sequence)
    for m in range(l- k + 1):
        word = ''
        # combine the followiing k letters to generate a kmer 
        for n in range(k):
            word = word + sequence[m+n]
        
        # save kmers in a list
        if word not in word_lists:
            word_lists.append(word)
        else:
            continue
    return len(word_lists)

# create the dataframe
def create_dataframe(l, sequence):
    observed_kmers_lists = []
    possible_kmers_lists = []
    k_lists = []
    
    for k in range(1,l+1):
        observed_kmers = kmers_observed(k, sequence)
        possible_kmers = kmers_possible(k, sequence)
        observed_kmers_lists.append(observed_kmers)
        possible_kmers_lists.append(possible_kmers)
        k_lists.append(k)
        
    df = pd.DataFrame({
        'k':k_lists,
        'Observed kmers':observed_kmers_lists,
        'Possible kmers':possible_kmers_lists,
    })
    
    
    df.set_index('k', inplace=True)
    
    
    return df

# draw the graph
def graph(df):
    x = df.index
    y1 = df["Observed kmers"]
    y2 = df["Possible kmers"]
    plt.figure(figsize = (10,7))
    plt.plot(x,y1,'ro',label = 'Observed kmers', alpha = 0.6, markersize = 10)
    plt.plot(x,y2,'b^',label = 'Possible kmers', alpha = 0.6, markersize = 10)
    plt.xlabel('k')
    plt.ylabel('kmers')
    plt.legend()
    plt.show()

# calculate the linguistic complexity
def complexity(df):
    sum_o = df["Observed kmers"].sum()
    sum_p = df["Possible kmers"].sum()
    return sum_o/sum_p

# main function
if __name__ == "__main__":
    sequence = 'ATTTGGATT'
    df = create_dataframe(9, sequence)
    print("========================================================================")
    print("This is the dataframe")
    print("========================================================================")
    print(df)
    print("========================================================================")
    print("The linguistic complexity is", complexity(df))
    print("========================================================================")
    graph(df)





