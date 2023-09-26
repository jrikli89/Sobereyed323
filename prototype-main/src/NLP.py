# integrate NLP library
import spacy 

# load English tokenizer, POS tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

def text_classification(text):
    doc = nlp(text)
    return doc.cats

def entity_recognition(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def language_modeling(text):
    doc = nlp(text)
    return [
        token.text
        for token in doc
        if token.is_stop != True and token.is_punct != True
    ]