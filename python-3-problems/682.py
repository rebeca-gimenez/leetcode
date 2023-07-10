'''
682. Baseball Game
Keep the scores for a baseball game with strange rules. 
You start with an empty record and are given a list of 
strings "operations", operations[i] is the ith operation
you must apply to the record:

An integer x. Record a new score of x.

'+'. Record a new score that is the sum of the prev. 2 scores.

'D'. Record a new score that is 2 times the previous score.

'C'. Invalidate the previous score, remove it from the record.

Return the sum of all the scores on the record after applying
all the operations.

The test cases are generated such that the answer 
and all intermediate calculations fit in a 32-bit 
integer and that all operations are valid.

1 <= operations.length <= 1000

operations[i] is "C", "D", "+", or a string representing 
an integer in the range [-3 * 104, 3 * 104].

For operation "+", there will always be at least two 
previous scores on the record.

For operations "C" and "D", there will always be at 
least one previous score on the record.
'''
def calPoints(ops):
    record = []
    for element in ops:
        if element == "C":
            record.pop()
        elif element == "D":
            record.append(record[-1]*2)
        elif element == "+":
            record.append(record[-1] + record[-2])
        else:
            record.append(int(element))
    return sum(record)


#Tests
ops = ["5","-2","4", "3"]
expected = 10
print(calPoints(ops), calPoints(ops)==expected)

ops = ["5","-2","4","C","D","9","+","+"]
expected = 27
print(calPoints(ops), calPoints(ops)==expected)

ops = ["5","2","C","D","+"]
expected = 30
print(calPoints(ops), calPoints(ops)==expected)

ops = ["1","C"]
expected = 0
print(calPoints(ops), calPoints(ops)==expected)