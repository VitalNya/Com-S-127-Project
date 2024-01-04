# tot_num_avail =
# stu_score =
# sum_score=
# av_score= (sum_score / tot_num_avail)

# Student ID,Name,Total Scores,Sum of All Scores,Score Average

# Student ID,Name,Total Scores,Sum of All Scores,Score Average  #END PRODUCT!!!!
# 123456,John Smith,5,408,81.6
# 654321,Jane Smith,3,147,49.0
# 246810,Trevor Smith,3,222,74.0
# 135791,Sally Smith,4,176,44.0

import FilesExerciseCalculations

def main():
    file2 = open("students.java", "r")  # We have grabbed the file
    file1 = open("scores.txt", "r")

    for i in file1:
        values = i.split()
        x = values[0]
        if x == '123456,' or x == '654321,':
            student_ID = "John Smith"
            print(x + student_ID)
        elif x == '246810,':
            student_ID = 'Trevor Smith'
            print(x + student_ID)
        elif x == '135791,':
            student_ID = 'Sally Smith'
            print(x + student_ID)


if __name__ == "__main__":
    main()


# print(student_ID + Name + tot_sco + sum_score + ave_score+)
