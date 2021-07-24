def largest_product(series, size):
    if len(series) < size:
        raise ValueError('Size > series')
    elif not series and size:
        raise ValueError('Empty series')
    elif series and not series.isdigit():
        raise ValueError('Series not digit')
    elif size < 0:
        raise ValueError('Negative size')
    elif size == 0:
        parts=[1]
    else:
        parts = []
        for i in range(len(series)):
            x = 1
            if i+size <= len(series):
                for j in range(i,i+size):
                    x *= int(series[j])
                parts.append(x)
    return max(parts)
