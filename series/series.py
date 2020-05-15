def slices(series, length):
    if length <= 0:
        raise ValueError("Desired length must be greater than 0!")
    if length > len(series):
        raise ValueError("Desired length is longer than series!")
    return [series[i:i+length] for i in range(0, len(series)) if i <= (len(series) - length)]
