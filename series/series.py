def slices(series, length):
    if length <= 0:
        raise ValueError("Desired length must be greater than 0!")
    if length > len(series):
        raise ValueError("Desired length is longer than series!")
    return [val for val in (series[i:i+length] for i, _ in enumerate(series)) if len(val) == length]