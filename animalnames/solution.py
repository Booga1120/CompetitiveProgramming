import sys

def main():
    beforeword = sys.stdin.readline().strip()
    lastletter = beforeword[-1]
    dictsize = int(sys.stdin.readline())
    dict = {}
    
    for i in range(dictsize):
        possibleword = sys.stdin.readline().strip()
        firstletter = possibleword[0]
        if (firstletter not in dict):
            dict[firstletter] = [possibleword]
        else:
            dict[firstletter].append(possibleword)
    
    if(lastletter not in dict):
        print("?")
    else:
        words = dict[lastletter]
        result = None
        
        for word in words:
            wordlastletter = word[-1]
            
            if wordlastletter not in dict:
                result = word
                break
            
            words_starting_with_ending = dict[wordlastletter]
            if len(words_starting_with_ending) == 1 and words_starting_with_ending[0] == word:
                result = word
                break
        
        if result:
            print(result + "!")
        else:
            print(words[0])

if __name__ == "__main__":
    main()