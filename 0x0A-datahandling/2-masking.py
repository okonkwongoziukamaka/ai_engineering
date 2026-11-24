# a program that mask a list of score

import numpy as np

scores = np.array([0.42, 0.91, 0.15, 0.78, 0.33])
mask = scores > 0.5
print(mask)
hi_score = scores[mask]
print(hi_score)

high_score = scores [scores > 0.5]
print(high_score)