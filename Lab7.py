def distance(word, word2):
    matrix = [[0 for i in range(len(word) + 1)] for j in range(len(word2) + 1)]
    # fill first row from 0 to n 
    for i in range(len(word) + 1):
        matrix[0][i] = i
    # fill first column from 0 to n 
    for i in range(len(word2) + 1):
        matrix[i][0] = i
    for i in range(len(word)):
        for j in range(len(word2)):
            # check to see if the character is the same to use the diagonal value
            if word[i] == word2[j]:
                matrix[i + 1][j + 1] = matrix[i][j]
            # get the smallest value surrounding it and add one to it
            else:
                matrix[i+1][j+1] = min(matrix[i][j], matrix[i][j+1], matrix[i+1][j]) + 1

    # return the last element of the matrix to obtain the final answer
    num_changes = matrix[len(word2)][len(word)]

    return num_changes


def main():
    word = "super"
    word2 = "duper"
    print("Test Case 1")
    print("Word 1: ", word)
    print("Word 2: ", word2)
    num_changes = distance(word, word2)
    print("Difference between words: ", num_changes)
    print()
    print("Test Case 2")
    word3 = "awesome"
    word4 = "someone"
    print("Word 3: ", word3)
    print("Word 4: ", word4)
    num_changes2 = distance(word3, word4)
    print("Difference between words: ", num_changes2)
    print()
    print("Test Case 3")
    word5 = "anywhere"
    word6 = "possible"
    print("Word 5: ", word5)
    print("Word 6: ", word6)
    num_changes3 = distance(word5, word6)
    print("Difference between words: ", num_changes3)

main()