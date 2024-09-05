# your code goes here!

class Anagram:
    def __init__(self,word) -> None:
        self.word = word

    def match(self,list_of_words):
        matches = []
        #list of letters of search word
        letters_to_search = [letter for letter in self.word]
        for word in list_of_words:
            letters = [ltr for ltr in word]                    #turn current word in loop into list of letters
            if sorted(letters) == sorted(letters_to_search):
                matches.append(word)
        return matches

anag1 = Anagram('listen')
anag1.match(['enlists', 'google', 'banana'])