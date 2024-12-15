class Solution:

    # def remove_word(self, sentence: str, word: str) -> str:
    #     # Split the sentence into words
    #     words = sentence.split()
    #     # Filter out the target word
    #     filtered_words = [w for w in words if w != word]
    #     # Join the filtered words back into a sentence
    #     return " ".join(filtered_words)

    # def count_spaces(sef, sentence: str) -> int:
    #     return sentence.count(" ")

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # words = sentence.split()
        # for index, indexWord in enumerate(words, start = 1):
        #     if indexWord[: len(searchWord)] == searchWord:
        #         return index
        # return -1

        return next((i for i, w in enumerate(sentence.split(), 1) if w.startswith(searchWord)), -1)
        