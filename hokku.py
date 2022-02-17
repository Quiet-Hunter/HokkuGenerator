# -*- coding: utf-8 -*-

import random


class Dictogram(dict):
    def __init__(self, iterable=None):
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable):

        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def return_random_word(self):
        # random.choice(histogram.keys())
        random_key = random.sample(self, 1)
        return random_key[0]

    def return_weighted_random_word(self):
        random_int = random.randint(0, self.tokens-1)
        index = 0
        list_of_keys = list(self.keys())
        for i in range(0, self.types):
            index += self[list_of_keys[i]]
            if(index > random_int):
                return list_of_keys[i]


def make_markov_model(data):
    markov_model = dict()

    for i in range(0, len(data)-1):
        if data[i] in markov_model:
            markov_model[data[i]].update([data[i+1]])
        else:
            markov_model[data[i]] = Dictogram([data[i+1]])
    return markov_model


def make_higher_order_markov_model(order, data):
    markov_model = dict()

    for i in range(0, len(data)-order):
        window = tuple(data[i: i+order])
        if window in markov_model:
            markov_model[window].update([data[i+order]])
        else:
            markov_model[window] = Dictogram([data[i+order]])
    return markov_model


def generate_random_start(model):
    # return random.choice(model.keys())
    if 'end' in model:
        seed_word = 'end'
        while seed_word == 'end':
            seed_word = model['end'].return_weighted_random_word()
        return seed_word
    return random.choice(model.keys())


def generate_random_sentence(markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    i = 0
    while current_word != 'end':
        i += 1
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weighted_word
        if current_word != 'end':
            sentence.append(current_word)
        # if i >= 5:
        #     break
    sentence[0] = sentence[0].capitalize()

    def random_end():
        ends = ['.']*75+['...']*10+['!']*10+['?']*5
        return random.choice(ends)

    return ' '.join(sentence) + random_end()
    # return sentence


def make_dict():
    DICTIONARY = []
    f = open('dictionary.txt', 'r')
    for line in f:
        # print(line)
        # text = line.decode('utf-8')
        DICTIONARY += line.lower().split()
    return DICTIONARY


def hokku():
    gap = '\n\n\t***\t\n'
    hokku = gap

    def make_string():
        model = make_markov_model(make_dict())
        text = generate_random_sentence(model)
        return text
    for i in range(0, 3):
        hokku += '\n'+make_string()
    hokku += gap
    print(hokku)
    return hokku


# >>> from hokku import hokku
