def summary(values):
    result = {}

    result["mean"] = mean(values)
    result["median"] = median(values)
    result["std_dev"] = std_dev(values)
    result["min"], result["max"] = min_max(values)
    return result

def sum(values):
    sum = 0
    for value in values:
        sum += value
    return sum

def mean(values):
    mean = sum(values) / len(values)
    return(mean) 

def median(values):
    median = 0
    if len(values)%2 == 0:
        median = (values[len(values)//2-1] + values[len(values)//2]) / 2
    else:
        median = values[len(values)//2]
    return median

def std_dev(values):
    avg = sum(values) / len(values)
    
    variance_sum =0
    for x in values:
        variance_sum += (x - avg) ** 2
    
    return (variance_sum / len(values)) ** 0.5

def min(values):
    min = values[0]
    for i in range(1, len(values)):
        if min > values[i]:
            min = values[i]
    return min

def max(values):
    max = values[0]
    for i in range(1, len(values)):
        if max < values[i]:
            max = values[i]
    return max

def min_max(values):
    return min(values), max(values)

data = [2, 4, 4, 4, 5, 5, 7, 9]
print(summary(data))