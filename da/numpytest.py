import numpy as np
import matplotlib.pyplot as plt
# a = np.arange(16).reshape(4,4)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(a.size)
# print(type(a))
#
# b = np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(b)

# c = np.zeros((3,4))
# print(c)
# c = np.ones((2,3,4),dtype=np.int32)
# print(c)
# c = np.empty((2,3))
# print(c)

# print(np.arange(10,30,5))

# from numpy import pi
# x = np.linspace(0,2*pi,30)
# print(x)

# d = np.arange(3)
# print(d)
# print(np.exp(d))

d = np.floor(10*np.random.random((3,4)))
print(d)
print(d.ravel())
print(d.reshape(6,2))



# def mandelbrot(h, w, maxit=20):
#     """Returns an image of the Mandelbrot fractal of size (h,w)."""
#     y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
#     c = x + y * 1j
#     z = c
#     divtime = maxit + np.zeros(z.shape, dtype=int)
#
#     for i in range(maxit):
#         z = z ** 2 + c
#     diverge = z * np.conj(z) > 2 ** 2  # who is diverging
#     div_now = diverge & (divtime == maxit)  # who is diverging now
#     divtime[div_now] = i  # note when
#     z[diverge] = 2  # avoid diverging too much
#
#     return divtime
# plt.imshow(mandelbrot(400,400))
# plt.show()

