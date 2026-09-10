students = [
    ["Neth", 90, 85, 95],
    ["Mike", 75, 80, 70],
    ["Jame", 88, 92, 84],
    ["Dara", 65, 78, 72],
    ["Sokha", 95, 89, 91]
]
print("--- Grading Student ---")
while True:
    userInput = int(input(
        "1. View Student Data\n"
        "2. Add Score Data\n"
        "3. Quit\n"
        "Choice: "
    ))
    if userInput == 1:
        print("--- View Student Data ---")
        for student in students:
            scores = student[1:]
            total = sum(scores)
            amounts = len(scores)
            avg = total / amounts
            print(f"Name {student[0]} | Score: {scores} | Average: {round(avg)}")
        back = int(input("--- Go Back? (Type 3 to get back) ---"))
        if back == 3:
          continue     
    elif userInput == 2:
        print("--- Add Score Data ---")
        name = input("Enter the student name: ")
        for student in students:
            if student[0].lower() == name.lower():
                print(f"=== ADD SCORE FOR STUDENT {name} ===")
                score = int(input("Enter Score: "))
                student.append(score)
                break
        else:
          print("Student Not Found")
          back = int(input("--- Go Back? (Type 3 to get back) ---"))
          if back == 3:
              continue
    elif userInput == 3:
        print("--- Quit ---")
        break