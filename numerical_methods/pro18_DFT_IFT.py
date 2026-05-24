import numpy as np
import matplotlib.pyplot as plt
n=int(input("Enter N: "))
fk=[]
for i in range(n):
    fk.append(complex(input(f"Enter fk{i}: ")))
print(fk)
Fp=[]
for p in range(n):
    fi=0
    for k in range(n):
        fi+= fk[k]*np.exp(-2*np.pi*1j*k*p/n)
    Fp.append(fi)
Fp_rounded = [complex(round(f.real, 3), round(f.imag, 3)) for f in Fp]
print(Fp_rounded)
# print("DFT :",Fp)
# Fp = np.array(Fp)
# plt.stem(np.abs(Fp))
# plt.xlabel("Frequency index")
# plt.ylabel("F[p] magnitude")
# plt.savefig("DFT_magnitude_spectrum.png")
# plt.show()