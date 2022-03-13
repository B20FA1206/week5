# 4. Диагональ нь 1-ийн тоо, бусад нь 0 байх 3x3 хэмжээтэй массив үүсгэ.

import numpy as np
a = np.zeros((3, 3), int)
np.fill_diagonal(np.fliplr(a), 1)
np.fill_diagonal(a, 1)
print(a)