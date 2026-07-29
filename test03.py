scores = list(map( int, input( 'score : ').split()))

total = 0
max_score = scores[0]
min_score = scores[0]
for i in range (len(scores)):
    total = total + scores[i]
    max_score = max_score if max_score > scores[i] else scores[i]
    min_score = min_score if min_score < scores[i] else scores[i]
    print ( f'scoere[{i}] = {scores[i]}')
print ( f'total score = {total}\t average score = {total / len(scores)}')
print ( f'max_score = {max_score}')
print ( f'min_score = {min_score}')






