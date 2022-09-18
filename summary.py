import cohere
import embeddings
co = cohere.Client('kVZ1RsPpqi2y7lX5tVZJX8fcD7mtFKIDlteoo0GB')


def readFile():
    with open('sample.txt') as f:
        read_data = f.read()
    str_list = list(filter(None, str.splitlines(read_data)))
    return str_list
    

def generateSummary(paragraphs: list) -> list:
    summary = []

    for i in paragraphs:
        while True:
            similarity = 0
            response = co.generate(
            model='large',
            prompt='Passage: Is Wordle getting tougher to solve? Players seem to be convinced that the game has gotten harder in recent weeks ever since The New York Times bought it from developer Josh Wardle in late January. The Times has come forward and shared that this likely isn’t the case. That said, the NYT did mess with the back end code a bit, removing some offensive and sexual language, as well as some obscure words There is a viral thread claiming that a confirmation bias was at play. One Twitter user went so far as to claim the game has gone to “the dusty section of the dictionary” to find its latest words.\n\nTLDR: Wordle has not gotten more difficult to solve, but people think it is.\n--\nPassage: For 15 years I have been single. For 15 years I\'ve longed for someone to call me their baby, their partner, their lover. For 15 years I\'ve asked myself, why has no one decided to put on me? I\'m confused and quite frankly, I just don\'t understand what don\'t I have. So today, ladies and gentlemen, especially the ladies. I shall be giving you a speech upon why. You should date me now. After intensive research upon the matter and after interviewing myself, I\'ve devised the list of reasons upon why all of you, all 30 of you, should be like Maria Victoria Pace. \n\nTLDR: I\'m a single woman with a list of reasons why you should date me.\n--\nFor years, there has been an ongoing battle between dog and cat lovers. Which furry friends make the best pets and companions? Although this has been debated for so long, the answer has always been clear. Dogs are a man’s best friend. They are loyal, compassionate, admiring, and loving. Studies have proven that people who own dogs are more likely to live longer and healthier lives. Where dogs are friendly and active, cats are aggressive and lazy. This means that dog owners are more likely to remain active on a daily basis whereas cat owners are likely to stay home. With all this, it is evident that there has never been much of a debate as dogs are the best pet one can have. \n\nTLDR: Dogs are better pets than cats.\n--\nWaffles or pancakes? The age-old question you hear at the hotel breakfast bar. Which one is better? Which is healthier, tastier, or just plain prettier? The thing is, although both may be great, neither one can compare to the classic that is french toast. The consistently beautiful presentation, the immaculate taste, and the wondrous side dishes that can be served with it. The list is endless. Rather than wasting time debating between waffles and pancakes, french toast should become the staple in all breakfast meals both at home, at hotels, and at various events. \n\nTLDR: French toast is the best breakfast food.\n--\n\n' + i + '\n\n TLDR:',
            max_tokens=80,
            temperature=0.4,
            k=0,
            p=1,
            frequency_penalty=0.02,
            presence_penalty=0,
            stop_sequences=["--"],
            return_likelihoods='NONE')
            temp_sum = response.generations[0].text
            similarity = embeddings.semantic_similarity(temp_sum, i)
            if similarity > 0.5:
                summary.append('Summary: {}'.format(response.generations[0].text))
                break
        
    return summary

print(generateSummary(readFile()))
    