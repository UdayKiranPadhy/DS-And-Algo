"""
Source :- Hashedin Exam(Akriti)



"""


def solution(S):
    S = [i for i in S]
    placed_Tanks = 0
    # 1st Place Tanks where it can cover more Houses
    for j in range(1,len(S)-1):
        if S[j] == '-':
            # If Place is vacant and Both sides are House
            if S[j-1] == S[j+1] == 'H':
                # Place a Tank
                S[j] = 'T'
                # Mark those Houses as Covered
                S[j-1] = 'O'
                S[j+1] = 'O'
                placed_Tanks += 1

    # Now Cover the houses which are left as it compulsary to cover a house and 
    # here we are keeping one tank for one House
    for i in range(len(S)):
        # Check if any house is uncovered
        if (i-1 >=0 and S[i-1] == 'H' and S[i]=='-') or (i+1 < len(S) and S[i+1] == 'H' and S[i]=='-'):
            S[i] = 'T'
            if S[i-1] =='H':
                S[i-1] = '0'
            else:
                S[i+1] = '0'
            placed_Tanks += 1
    
    if 'H' in S:
        return -1
    return placed_Tanks
