import numpy as np

subreddits = ['CMU', 'UIUC', 'MIT', 'stanford', 'UCSD', 'berkeley', 'cornell', 'uofm', 'udub', 'umd', 'gatech',
              'neu', 'columbia', 'uwmadison', 'upenn', 'utaustin', 'purdue', 'umass', 'nyu', 'ucla']
n = len(subreddits)
backMap = {}
texts = []
for sub in subreddits:
    backMap[sub] = subreddits.index(sub)
    file = open(sub + '.txt')
    texts.append(file.read().lower())

M = np.zeros((n, n))
for sub1 in subreddits:
    for sub2 in subreddits:
        if sub1 == sub2:
            continue
        sub1_idx = backMap[sub1]
        sub2_idx = backMap[sub2]
        M[sub2_idx][sub1_idx] = texts[sub1_idx].count(sub2.lower())


beta = 0.85
for col in range(len(subreddits)):
    denom = np.sum(M[:, col])
    for row in range(len(subreddits)):
        if denom != 0:
            M[row][col] /= denom
A = beta * M + (1-beta) * (1/n) * np.ones((n, n))

iter = 0
diff = 9999
ranks = np.ones((n, ))
while iter < 1000 and diff > 0.00000001:
    new_ranks = A.dot(ranks)
    diff = np.sum(np.abs(ranks - new_ranks))
    ranks = new_ranks
    iter += 1

print('RANKS')
for sub in subreddits:
    print(sub + ': ' + str(ranks[backMap[sub]]))
