# replaces nan items from a series with a given value
def fillna(series, filler=0):
    import math
    result = []
    for i in series:
        if i == None or math.isnan(i):
            result.append(filler)
        else:
            result.append(i)
    return result

# average of the series
def mean(series):
    s = series.copy()
    while None in s:
        s.remove(None)
    while -999 in s:
        s.remove(-999)
    if (len(s)) == 0:
        return None
    return sum(s) / float(len(s))

# standard deviateion of the series
def standard_deviation(series):
    return variance(series) ** (1.0/2.0)

# statistal variance of the series
def variance(series):
    series_mean = mean(series)
    return sum([(x-series_mean)**2.0 for x in series]) / len(series)

# executes a rule against each item in a series and returns matches, rule should be a lambe
# matches(data, lambda x: x > 2)
# list comprehension is slower compared to loops for shorter lists but faster for longer lists
def matches(series, rule):
    return [i for i, item in enumerate(series) if rule(item)]

# applied a function to a series of values, formula should be a lambda
# f_x(data, lambda x: 3x + 2)
def f_x(series, formula):
    return [formula(item) for item in series]

def series_diff(series_a, series_b, adjustment=None):
    if len(series_a) != len (series_b):
        raise Exception('series_diff: two series must be the same length')
    if adjustment == None:
        adjustment = mean(series_a)
    series = []
    for i in range(len(series_a)):
        series.append(series_a[i] - series_b[i] + adjustment)
    return series
