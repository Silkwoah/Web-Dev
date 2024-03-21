if __name__ == '__main__':

    n_eng = int(input().strip())
    
    eng_subs = set(map(int, input().split()))
    
    n_french = int(input().strip())
    
    french_subs = set(map(int, input().split()))
    
    result = eng_subs.symmetric_difference(french_subs)
    
    print(len(result))
