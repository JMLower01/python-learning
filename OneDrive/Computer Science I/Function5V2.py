def main():
    name = get_student_name()
    scores = get_validated_scores()
    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(average)
    display_report(name, scores, average, grade, standing)
    test_grade_tracker()
    
        

def get_student_name():
    return input("Student name: ")

def get_validated_scores():
    while True:
        scores = get_exam_scores()
        if len(scores) == 3:
            return scores
        else:
            print("Invalid scores, try again.")
            

def get_exam_scores():
    scores = []
    for i in range(3):
            score_str = (input(f"Exam {i+1} score: "))
            if is_valid_score(score_str):
               score = int(score_str)
               scores.append(score)
            else:
                print("Invalid!")
                continue
    return scores

def is_valid_score(score_str):
    if score_str.isdigit():
        score = int(score_str)
        if 0 <= score <= 100:
            return True
        else:
            return False
    else: 
        return False


def calculate_average(scores):
    """
    Calculates average of a list of scores.
    Args:
        scores (list):  Scores to be calculated

    Returns:
        float: The average score in the list
    """
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def determine_letter_grade(average):
    """
    Determines the grade based off of the average

    Args:
        average (float): Average exam score

    Returns:
        string: Letter grade
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def determine_standing(average):
    if average >= 90:
        return "Dean's List"
    elif average >= 70:
        return "Good Standing"
    elif average >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"

def display_report(name, scores, average, grade, standing):
    print("=" * 30)
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print("=" * 30)

def test_grade_tracker():
    
    # Testing calculate_average
    
    # Test 1: empty list
    result = calculate_average([])
    expected = 0
    if result == expected:
       print("PASS") 
    else:
        print(f"FAIL: Got {result}, expected {expected}")
        
    # Test 2: All zeroes
    result = calculate_average([0, 0, 0])
    expected = 0
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
        
    # Test 3: Normal scores
    result = calculate_average([80, 70, 90])
    expected = 80.0
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
    
    # Testing determine_letter_grade
    
    # Test 1: score of 0
    
    result = determine_letter_grade(0.0)
    expected = "F"
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
    
    # Test 2: boundary score
    
    result = determine_letter_grade(80.0)
    expected = "B"
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
    
    # Test 3: normal score
    result = determine_letter_grade(76.5)
    expected = "C"
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
    
    # Test 4: perfect score
    result = determine_letter_grade(100.0)
    expected = "A"
    if result == expected:
        print("PASS")
    else:
        print(f"FAIL: Got {result}, expected {expected}")
        

main()