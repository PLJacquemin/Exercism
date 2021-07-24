def flatten(iterable):
    flat = False
    while not flat:
        output = []
        flat = True
        for i in iterable:
            # if list still in iterable, continue while
            if isinstance(i, list):
                flat = False
                for j in i:
                    output.append(j)
            elif i == None:
                continue
            else:
                output.append(i)
        iterable = output
    return output
