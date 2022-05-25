from inspector import Code


class SentenceGroup:
    def __init__(self):
        self.sentence = None
        self.sentence_value = ""
        self.sentence_offset_start = 0
        self.sentence_offset_end = 0
        self.sentence_value_with_offset = ""
        self.words_to_inspect = []
        self.error_words = []

    def set_data(self, data):
        if data[Code.T_VALUE_INDEX] == Code.SENTENCE:
            self.set_sentence_data(data)
        elif data[Code.T_VALUE_INDEX] not in Code.NOT_WORD:
            self.words_to_inspect.append(data)

    def set_sentence_data(self, data):
        self.sentence = data
        self.sentence_value = data[Code.S_VALUE_INDEX]
        self.sentence_offset_start = data[Code.OFFSET_START_INDEX]
        self.sentence_offset_end = data[Code.OFFSET_END_INDEX]
        self.sentence_value_with_offset = '[{offset}]{char}'.format(offset=self.sentence_offset_start, char="")
        for idx, val in enumerate(self.sentence_value, 1):
            self.sentence_value_with_offset += '{char}[{offset}]'.format(char=val, offset=self.sentence_offset_start + idx)

    def inspect_sentence(self):
        offset_end = self.sentence_offset_start + len(self.sentence_value) + Code.OFFSET_ADD_FOR_SPEECH_SENTENCE
        if self.sentence_offset_end != offset_end:
            self.error_words.append(self.sentence)

    def inspect_words(self):
        for word in self.words_to_inspect:
            word_from_sentence = self.substr_word_from_sentence_by_offset(word)
            if word[Code.S_VALUE_INDEX] != word_from_sentence:
                self.error_words.append(word)

    def substr_word_from_sentence_by_offset(self, word):
        word_offset_start = word[Code.OFFSET_START_INDEX] - self.sentence_offset_start
        word_offset_end = word[Code.OFFSET_END_INDEX] - self.sentence_offset_start
        return self.sentence_value[word_offset_start:word_offset_end]
