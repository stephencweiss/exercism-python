def classify(number):
    if number <= 0:
        raise ValueError("Classification works only for positive integers")
    if sum(factors_of_n(number)) == number:
        return "perfect"
    elif sum(factors_of_n(number)) < number:
        return "deficient"
    elif sum(factors_of_n(number)) > number:
        return "abundant"


def factors_of_n(number):
    return [factor for factor in range(1, int(number/2)+1) if number % factor == 0]
