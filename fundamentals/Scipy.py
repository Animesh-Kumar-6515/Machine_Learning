# scipy is a python library for scintific caluclation

from scipy import special

a=special.exp10(2) #will calculate 10^2
print(a)
b=special.exp2(3) #will calculate 2^3
print("b: ",b)

# sin cosine function

c=special.sindg(30)
print(c)
d=special.cosdg(30)
print(d)

#integratin function
from scipy import integrate
#quad function calculate inegral of a equation with only one value
i=integrate.quad(lambda x:special.exp10(x),0,1)
print(i)

#solve double integral function



# fourier transformation
from scipy.fftpack import fft,ifft
import numpy as np
x=np.array([1,2,3,4])
y=ifft(x)
# y=fft(x)
print (y)


# Linear algerbra
from scipy import linalg
arr=np.array([[1,2],[3,4]])
brr=linalg.inv(arr)
print(b)

# interplation -  Its refers to constructing new data points within a set of know data points
import matplotlib.pyplot as plt
from scipy import interpolate
ax=np.arange(5,20)
ay=np.exp(ax/3.0)
f=interpolate.interp1d(ax,ay)
newax=np.arange(6,12)
neway=f(newax)
plt.plot(ax,ay,'o',newax,neway,'--')
plt.show()