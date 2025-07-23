import streamlit as st

st.info("""
# Aplikasi Cek Gaji Pokok
""")
st.warning("Ini adalah aplikasi untuk mengecek Gaji Pokok Berdasarkan Masa Kerja dan Golongan")

tipe_pegawai = ["Pilih Tipe Pegawai", "Pegawai Negeri Sipil (PNS)", "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)"]
golongan_pegawai = ["Pilih Golongan",
                 "Golongan Ia",
                 "Golongan Ib",
                 "Golongan Ic",
                 "Golongan Id",
                 "Golongan IIa",
                 "Golongan IIb",
                 "Golongan IIc",
                 "Golongan IId",
                 "Golongan IIIa",
                 "Golongan IIIb",
                 "Golongan IIIc",
                 "Golongan IIId",
                 "Golongan IVa",
                 "Golongan IVb",
                 "Golongan IVc",
                 "Golongan IVd",
                 "Golongan IVe",
                 "Golongan I",
                 "Golongan II",
                 "Golongan III",
                 "Golongan IV",
                 "Golongan V",
                 "Golongan VI",
                 "Golongan VII",
                 "Golongan VIII",
                 "Golongan IX",
                 "Golongan X",
                 "Golongan XI",
                 "Golongan XII",
                 "Golongan XIII",
                 "Golongan XIV",
                 "Golongan XV",
                 "Golongan XVI",
                 "Golongan XVII"]
masa_kerja = ["Pilih Masa Kerja", 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
                 

tipe_pegawaii = st.selectbox(''':blue[Masukan Tipe Pegawai]''', tipe_pegawai)
golongan_pegawaii = st.selectbox(''':blue[Masukan Golongan]''', golongan_pegawai)
masa_kerjaa = st.selectbox(''':blue[Masukan Masa Kerja (Dalam Tahun)]''',masa_kerja)

# Golongan Ia
if tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 1.685.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 1.738.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 1.793.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 1.850.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 1.908.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 1.968.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 2.030.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 2.094.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 2.160.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 2.228.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 2.298.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 2.370.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 2.445.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
# Golongan Ib  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.840.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 1.898.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 1.958.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.020.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.083.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.149.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.217.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.287.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.359.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.433.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.510.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 2.589.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.670.700")
  
# Golongan Ic 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.918.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 1.979.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.041.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.105.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.172.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.240.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.311.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.383.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.458.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.536.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.616.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 2.698.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.783.700")
  
# Golongan Id
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.999.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.062.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.127.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.194.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.264.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.335.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.408.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.484.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.562.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.643.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.726.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 25 <= masa_kerjaa <=26:
  st.warning ("Gaji Pokoknya adalah 2.812.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.901.400")
   
# Golongan IIa 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 0 <= masa_kerjaa <= 0:
  st.warning ("Gaji Pokoknya adalah 2.184.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 1 <= masa_kerjaa <= 2:
  st.warning ("Gaji Pokoknya adalah 2.218.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.288.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.360.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.434.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.511.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.590.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.672.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.756.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.843.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.932.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.024.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.120.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.218.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.319.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.424.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.532.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.643.400")  

# Golongan IIb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.385.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.460.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.537.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.617.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.700.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.785.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.872.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.963.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.056.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.152.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.252.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.354.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.460.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.569.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.681.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.797.500")

# Golongan IIc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.485.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.564.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.645.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.728.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.814.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.902.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.994.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.088.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.185.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.286.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.389.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.496.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.606.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.720.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.837.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.958.200")

# Golongan IId
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.591.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.672.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.756.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.843.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.933.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.025.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.120.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.219.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.320.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.425.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.533.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.644.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.759.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.877.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.999.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.125.600")

# Golongan IIIa
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 2.785.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 2.873.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 2.964.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.057.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.153.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.252.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.355.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.461.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.570.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 3.682.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 3.798.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 3.918.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.041.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.168.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.300.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.435.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.575.200")

# Golongan IIIb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 2.903.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 2.995.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.089.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.186.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.287.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.390.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.497.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.607.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.721.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 3.838.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 3.959.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.083.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.212.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.345.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.482.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.623.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.768.800")

# Golongan IIIc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.026.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.121.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.220.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.321.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.426.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.533.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.645.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.760.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.878.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.000.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.126.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.256.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.390.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.528.900")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.671.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.818.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.970.500")

# Golongan IIId 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.154.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.253.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.356.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.461.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.571.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.683.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.799.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.919.100")

 elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.042.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.169.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.301.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.436.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.576.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.720.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.869.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.022.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.180.700")

# Golongan IVa
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.287.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.391.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.498.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.608.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.722.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.839.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.960.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.084.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.213.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.346.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.483.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.624.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.770.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.920.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.075.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.235.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.399.900")

# Golongan IVb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.426.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.534.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.646.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.761.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.879.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.001.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.127.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.257.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.391.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.530.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.672.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.819.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.971.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.128.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.289.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.456.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.628.300")

# Golongan IVc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.571.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.684.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.800.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.920.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.043.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.170.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.302.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.437.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.577.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.721.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.870.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.023.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.182.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.345.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.513.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.687.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.866.400")

# Golongan IVd 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.723.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.840.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.961.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.085.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.214.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.347.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.484.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.625.500")

 elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.771.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.921.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.076.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.236.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.401.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.571.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.746.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.927.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.114.500")

# Golongan IVe 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.880.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.002.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.128.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.258.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.392.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.531.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.673.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.821.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.973.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.129.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.291.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.457.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.629.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.807.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.989.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.178.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.373.200")




