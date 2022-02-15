
import DFT
def test_cal_FFT_4():
   size= 4
   a, b, c = DFT.create_np_array(size,dtype=complex)
   Xr,Xi = DFT.cal_FFT(c, b, c, b, size)
   Xfft = Xr + 1j * Xi
   Xstd = DFT.cal_FFT_std(a)
   assert Xfft.all() == Xstd.all()
def test_cal_FFT_16():
   size= 16
   a, b, c = DFT.create_np_array(size,dtype=complex)
   Xr,Xi = DFT.cal_FFT(c, b, c, b, size)
   Xfft = Xr + 1j * Xi
   Xstd = DFT.cal_FFT_std(a)
   assert Xfft.all() == Xstd.all()
def test_cal_FFT_64():
   size= 64
   a, b, c = DFT.create_np_array(size,dtype=complex)
   Xr,Xi = DFT.cal_FFT(c, b, c, b, size)
   Xfft = Xr + 1j * Xi
   Xstd = DFT.cal_FFT_std(a)
   assert Xfft.all() == Xstd.all()
def test_cal_FFT_256():
   size= 256
   a, b, c = DFT.create_np_array(size,dtype=complex)
   Xr,Xi = DFT.cal_FFT(c, b, c, b, size)
   Xfft = Xr + 1j * Xi
   Xstd = DFT.cal_FFT_std(a)
   assert Xfft.all() == Xstd.all()
