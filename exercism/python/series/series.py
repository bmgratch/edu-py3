def slices(series, length):
    # Test for length errors
    if (length < 1) or (length > len(series)):
        raise ValueError('Inappropriate length')
    i = 0
    result = []
    while (i + length) < (len(series) + 1):
        result.append(series[i:i+length])
        i += 1
    return(result)
