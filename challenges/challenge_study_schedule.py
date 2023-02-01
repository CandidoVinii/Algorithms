def study_schedule(permanence_period, target_time):
    if not target_time and target_time != 0:
        return None

    students = 0

    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time <= end:
            students += 1

    return students
