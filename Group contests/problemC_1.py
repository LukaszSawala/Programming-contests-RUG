n = int(input())
prices = [int(i) for i in input().split()]
length = len(prices)
q = int(input())
curr_inflation = 0
curr_sum = sum(prices)

'''
word_freq = dict()
corpus_word = str(corpus).split()
for word in range(len(corpus_ref)):
    if corpus_word[word] not in word_freq:
        word_freq[corpus_word[word]] = 1

    else:
         word_freq[corpus_word[word]] += 1'''

for i in range(q):
    action = input().split()
    if action[0] == "INFLATION":
        curr_inflation += int(action[1])
    else:
        toChange = int(action[1])
        new = int(action[2])
        for j in range(length):
            if prices[j] + curr_inflation == toChange:
                prices[j] = new - curr_inflation
        curr_sum = sum(prices)
    print(curr_sum + length*curr_inflation)