def convert(number):
    result = ''
    if 0 != number % 3 and 0 != number % 5 and 0 != number %7:
        return str(number)
    if 0 == number % 3:
        result += "Pling"
    if 0 == number % 5:
        result += "Plang"
    if 0 == number % 7:
        result += "Plong"
    return result


