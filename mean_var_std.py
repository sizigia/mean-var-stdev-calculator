import numpy as np


def calculate(list_):
    if len(list_) < 9:
        raise ValueError("List must contain nine numbers.")
    m = np.array(list_).reshape(3, 3)
    axis_ = [0, 1, None]  # [axis1 (rows), axis2 (columns), flattened]
    measures = {
        'mean': lambda x, y: x.mean(y),
        'variance': lambda x, y: x.var(y),
        'standard deviation': lambda x, y: x.std(y),
        'max': lambda x, y: x.max(y),
        'min': lambda x, y: x.min(y),
        'sum': lambda x, y: x.sum(y)}

    calculations = {measure: [func(m, a).tolist() for a in axis_]
                    for measure, func in measures.items()}

    return calculations
