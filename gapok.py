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
                 "Golongan IVe"]
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
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
# Golongan Id
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  



