# 6. Хоёр хэмжээст массив үүсгэж нийт элементүүдийн нийлбэр, багана, мөрийн нийлбэрүүдийг хэвлэ.

import numpy as np

a = [[1, 2, 3], [1, 2, 3]]

arr = np.array(a)

print('мөр:',  arr.sum(axis=1))
print('багана:',  arr.sum(axis=0))
print('нийт:', arr.sum())