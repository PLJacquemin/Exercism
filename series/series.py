def slices(series, length):
    slist = []
    if not series or length <= 0 or length > len(series):
        raise ValueError("empty series or invalid length")
    for i in range(len(series)-(length-1)):
        slist.append(series[i:i+length])
    return slist
