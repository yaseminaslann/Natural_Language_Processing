# -*- coding: utf-8 -*-


import re
import string
from nltk.corpus import stopwords


class Make_Str:
    def process(self, text):
        return str(text)

class Replace_By:
    def __init__(self, replace_by):
        self.replace_by = replace_by
    def process(self, text):
        for replace, by in self.replace_by:
            text = text.replace(replace, by)
        return text

class Lower_Str:
    def process(self, text):
        return text.lower()

class Text_To_Vector:
    def __init__(self, seperator=' '):
        self.seperator = seperator
    def process(self, text):
        words_vector = text.split(self.seperator)
        return words_vector

class Remove_HTML:
    def process(self,words_vector):
        rule = re.compile(r'<.*?>')
        return [rule.sub('',word) for word in words_vector]
    
class Filter_Punctuation:
    def __init__(self, punctuations=string.punctuation):
        self.punctuations = punctuations
    def process(self, words_vector):
        rule = re.compile('[%s]'%re.escape(self.punctuations))
        return [rule.sub('', word) for word in words_vector]

class Filter_Non_Alpha:
    def process(self, words_vector):
        return [word for word in words_vector if word.isalpha()]

class Filter_Stop_Word:
    def __init__(self, language):
        self.stopwords_ = set(stopwords.words(language))
    def process(self, words_vector):
        return [word for word in words_vector if not word in self.stopwords_]


class Vector_To_Text:
    def process(self, words_vector):
        return ' '.join(words_vector)

class Text_Processor:
    def __init__(self, processor_list):
        self.processor_list = processor_list
    def process(self, text):
        for processor in self.processor_list:
            text = processor.process(text)
        return text


class DocumentProcessor:
    def  __init__(self, textProcessor):
        self.textProcessor = textProcessor
    def process(self, docs):
        return [self.textProcessor.process(doc) for doc in docs]


replace_by = [('.',''), (',',''), (';',''), ('?',''), ('!',''), ('İ','i')]
processors = [Make_Str(),
              Replace_By(replace_by = replace_by),
              Lower_Str(),
              Text_To_Vector(),
              Remove_HTML(),
              Filter_Punctuation(),
              Filter_Non_Alpha(),
              Filter_Stop_Word(language='English'),
              Vector_To_Text()]

text_processor = Text_Processor(processor_list = processors)
document_processor = DocumentProcessor(textProcessor = text_processor)
