# Vital Nyabashi
# lab 1
# Week 12 : countGoal


def countDownGoal(n, goal):
    if n < goal:
        print("Goal!")
    else:
        # print(n)
        countDownGoal(n-1, goal)
        print(n)


def oppositeCountDownGoal(n, goal):
    if n < goal:
        print("Goal!")
    else:
        print(n)
        oppositeCountDownGoal(n-1, goal)


def main():
    countDownGoal(5, 3)
    print('------------------------------')
    oppositeCountDownGoal(5, 3)


if __name__ == "__main__":
    main()
