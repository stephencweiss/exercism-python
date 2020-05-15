def classify(number):
    if number <= 0:
        raise ValueError("Classification works only for positive integers")
    aliquot_sum = find_aliquot_sum(number)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum < number:
        return "deficient"
    elif aliquot_sum > number:
        return "abundant"


def find_aliquot_sum(number):
    return sum(factor for factor in range(1, int(number/2)+1) if number % factor == 0)
