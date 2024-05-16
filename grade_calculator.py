def calculate_gpa(grades):
    total_grade_point=sum(grades.values())
    total_courses=len(grades)
    if total_courses==0:
        return 0
    return total_grade_point/total_courses

    