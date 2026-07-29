scores = list(map( int, input( 'score : ').split()))
print (scores)

# 最大值 最小值 平均數

print ( f'average = {(scores [0] + scores [1] + scores [2]) / 3}') 

max_score = scores[0] if scores[0] > scores[1] else scores[1]
max_score = scores[2] if scores[2] > max_score else max_score
print ( f'max score = {max_score}')

min_score = scores[0] if scores[0] > scores[1] else scores[1]
min_score = scores[2] if scores[2] > min_score else min_score
print ( f'min score = {min_score}')

