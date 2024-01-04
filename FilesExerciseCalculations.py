scores = {}

# Read score data from file and count scores for each ID number
file1 = open('scores.txt', "r")
file2 = open('students.java', "r")
def main():

    for line in file1:
        parts = line.strip().split(', ')
        id_number = parts[0]
        score = int(parts[2])
        if id_number not in scores:
            scores[id_number] = [score, 1]
        else:
            scores[id_number][0] += score
            scores[id_number][1] += 1

    students = []

    for line in file2:
        parts = line.strip().split(', ')
        students.append(parts)
        names = parts[0]

    print(students)

    for student in students:
        x = student[0]
        print(scores[x], student[0], student[1])
        names2 = (scores[x], student[0], student[1])


    #
    # Compute total scores, sum of all scores, and score average for each student
    for id_number, count in scores.items():
        total_scores = count[1]
        sum_scores = count[0]
        score_average = sum_scores / total_scores
        print(f"Student with ID number {id_number} , {students} has {count} scores, a total score of {sum_scores}, and an average score of {score_average:.2f}.")

if __name__ == "__main__":
    main()

