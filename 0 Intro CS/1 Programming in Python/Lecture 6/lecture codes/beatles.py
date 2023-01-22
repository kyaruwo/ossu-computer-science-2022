she_loves_you = [
    'she', 'loves', 'you', 'yeah', 'yeah',
    'yeah', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

    'you', 'think', "you've", 'lost', 'your', 'love',
    'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
    "it's", 'you', "she's", 'thinking', 'of',
    'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'she', 'said', 'you', 'hurt', 'her', 'so',
    'she', 'almost', 'lost', 'her', 'mind',
    'and', 'now', 'she', 'says', 'she', 'knows',
    "you're", 'not', 'the', 'hurting', 'kind',

    'she', 'says', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',

    'you', 'know', "it's", 'up', 'to', 'you',
    'i', 'think', "it's", 'only', 'fair',
    'pride', 'can', 'hurt', 'you', 'too',
    'pologize', 'to', 'her',

    'Because', 'she', 'loves', 'you',
    'and', 'you', 'know', 'that', "can't", 'be', 'bad',
    'Yes', 'she', 'loves', 'you',
    'and', 'you', 'know', 'you', 'should', 'be', 'glad',

    'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'with', 'a', 'love', 'like', 'that',
    'you', 'know', 'you', 'should', 'be', 'glad',
    'yeah', 'yeah', 'yeah',
    'yeah', 'yeah', 'yeah', 'yeah'
]


def lyrics_to_frequencies(lyrics):
    frequency_dict = {}
    for word in lyrics:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict


beatles = lyrics_to_frequencies(she_loves_you)
# print(beatles)


def most_common_words(freqs):
    words = []
    best = max(freqs.values())
    for (word, freq) in freqs.items():
        if freq == best:
            words.append(word)
    return (words, best)


def words_often(freqs, minTimes):
    res = []
    while True:
        words, best = most_common_words(freqs)
        if best >= minTimes:
            res.append((words, best))
            for word in words:
                del (freqs[word])
        else:
            return res


print(words_often(beatles, 5))
