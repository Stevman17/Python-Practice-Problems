#Given that a student answered a question correctly, what is the probability that she really knows the material?
#Priors:
#(1)There is a question on the exam that 60% of students know the correct answer to.
#(2)Given that a student knows the correct answer, there is still a 15% chance that the student picked the wrong answer.
#(3)Given that a student does not know the answer, there is still a 20% chance that the student picks the correct answer by guessing.

#In order to use Bayes Theorem, we need to phrase our question as P(A|B). What is A and B in this case?
#Answer: P(knows the material | answers correctly)
#Answer: (A knows the material) given (B answers correctly)
# What is the probability that the student knows the material?
knows_the_material = 0.60
#Given that the student knows the material, what is the probability that she answers correctly?
answers_correctly_given_knows_material = 1 -.15
#What is the probability of any student answering correctly?
any_student_correct_answer = (.2*.4)+(knows_the_material*answers_correctly_given_knows_material)
#Using the three probabilities and Bayes' Theorem, calculate P(knows material | answers correctly).
P_knows_and_answers = (answers_correctly_given_knows_material * knows_the_material) / any_student_correct_answer

print P_knows_and_answers
