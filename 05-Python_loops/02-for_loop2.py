student_score=[10,9,8,7,6]
print(max(student_score))

max_score=0
for score in student_score:
    if(score>max_score):
        max_score=score

print(max_score)