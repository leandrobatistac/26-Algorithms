def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for inicio, fim in permanence_period:
            if inicio <= int(target_time) <= fim:
                counter += 1
    except TypeError:
        return None

    return counter