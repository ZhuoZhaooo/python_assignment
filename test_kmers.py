from kmers import *

# test the kmers_possible function 
# given k = 6, expectation is 4
def test_kmers_possible():
    sequence = 'ATTTGGATT'
    k = 6
    obs = kmers_possible(k, sequence)
    exp = 4
    assert  obs ==exp
    
# test the kmers_observed function
# given k = 4, expectation is 6
def test_kmers_observed():
    sequence = 'ATTTGGATT'
    k = 4
    obs = kmers_observed(k, sequence)
    exp = 6
    assert obs == exp

# test the contents in the data frame
def test_create_dataframe():
    sequence = 'ATTTGGATT'
    df = create_dataframe(9, sequence)
    obs_observed_kmers = df["Observed kmers"].tolist()
    obs_possible_kmers = df["Possible kmers"].tolist()
    
    # the expectation results for each column
    # test it in the form of list
    exp_observed_kmers = [3,5,6,6,5,4,3,2,1]
    exp_possible_kmers = [4,8,7,6,5,4,3,2,1]
    
    for i in range(0,9):
        assert obs_observed_kmers[i] == exp_observed_kmers[i]
        assert obs_possible_kmers[i] == exp_possible_kmers[i]
        
# test the complexity function
# the expectation result is 0.875
def test_complexity():
    sequence = 'ATTTGGATT'
    df = create_dataframe(9, sequence)
    exp = complexity(df)
    assert exp == 0.875 
        
    
