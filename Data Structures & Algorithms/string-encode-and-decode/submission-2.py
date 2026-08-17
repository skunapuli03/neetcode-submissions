class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode takes each word and stores into a array
        total = []
        #or it stores into array, but after each word u add a hashtag or some identifyer
        for word in strs:
            total.append(str(len(word))+"#"+word)
        #this is the concatenation part after adding the hashtag/identifyer
        return "".join(total)
    def decode(self, s: str) -> List[str]:
        #look for the hashtag so i can read teh length of the word before it
        #then read exactlly how manyu characters after # as one word
        #combine that word to my result list, and this process is repeated

        result = []
        #this i marks wghere teh encoded word starts
        i = 0

        while i < len(s):
            #move j until u find the #
            j = i
            while s[j]!="#":
                j+=1
            word_len = int(s[i:j])

            word_strt = j+1

            word = s[word_strt: word_strt+word_len]

            result.append(word)

            i = word_strt+word_len
        return result

