if __name__ == '__main__':
    n_eng = int(input().strip())
    
    eng_subs = set(map(int, input().split()))
    
    n_french = int(input().strip())
    
    french_subs = set(map(int, input().split()))
    
    eng_only_subs = eng_subs.difference(french_subs)
    
    print(len(eng_only_subs))
