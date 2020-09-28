class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}
        for i in range(97, 96 + (len(morse_code) + 1)):
            dic[chr(i)] = morse_code[i - 97]
        words_to_morse = []
        for word in words:
            t_s = ''
            for i in word:
                t_s += dic[i]
            words_to_morse.append(t_s)

        return len(set(words_to_morse))
