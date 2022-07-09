import numpy as np

df1 = df[df['유종'] == '휘발유']
x = df1['배기량'].astype(float)
y = df1['CO2배출량'].astype(float)

mean_x, mean_y = np.mean(x), np.mean(y)
xy = np.sum((x - mean_x)*(y - mean_y))
xx = np.sum((x - mean_x)**2)
a = xy/xx
b = mean_y - a * mean_x

print('예측 모델 식: y =', b, '* x +', a)
