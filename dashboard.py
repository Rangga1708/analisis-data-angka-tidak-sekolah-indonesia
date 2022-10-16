import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.title("Alokasi Dana untuk Pendidikan, Perlukah?")

image = Image.open('Pendidikan.jpg')
st.image(image)

'''
Masyarakat Indonesia saat ini dihebohkan dengan keputusan pemerintah untuk
menaikkan harga BBM bersubsidi. Pertalite yang semula dapat dibeli dengan harga
Rp7.650 per liter naik menjadi Rp10.000 per liter, sedangkan Solar yang semula 
dapat dibeli seharga Rp5.150 per liter juga naik menjadi Rp6.800 per liter.
'''

st.header('Mengapa BBM Naik?')

'''
Walaupun demikian, naiknya harga BBM bukan dilakukan tanpa alasan. Menteri Keuangan Sri Mulyani
mengatakan bahwa anggaran untuk subsidi dan kompensasi pada tahun 2022 mencapai
Rp502,4 triliun, di mana angka tersebut sudah melewati batas alokasi awal. Salah satu
kemungkinan penyebab hal tersebut adalah sasaran subsidi yang kurang tepat. Subsidi
yang seharusnya diberikan kepada masyarakat kurang mampu, ternyata justru lebih
banyak dinikmati oleh masyarakat yang mampu.
'''

'''
Dengan menaikkan harga BBM, artinya jumlah subsidi untuk BBM akan dikurangi dan
dapat dialokasikan untuk keperluan lainnya. Pertanyaannya adalah akan dialokasikan
ke mana biaya subsidi tersebut?
'''

st.header('Pendidikan Indonesia Saat Ini')

'''
Salah satu sektor yang perlu perhatian khusus adalah sektor pendidikan. Ketua 
Kelompok Kerja Pendidikan G20, Iwan Syahril mengatakan bahwa dunia pendidikan
terancam *learning loss* sebagai akibat dari pandemi Covid-19. *Learning loss*
ini biasanya terjadi pada kelompok masyarakat ekonomi menengah ke bawah. Grafik
di bawah ini menunjukkan jumlah anak Indonesia yang tidak bersekolah pada rentang
tahun 2019-2021.
'''

data = pd.read_csv('https://raw.githubusercontent.com/Rangga1708/analisis-data-angka-tidak-sekolah-indonesia/main/AATS%20Pengeluaran.csv')
data['Tahun'] = pd.to_datetime(data['Tahun'], format='%Y')
data['Persentase'] = data['Persentase'].map(lambda x: x/100)

jenjang = st.selectbox(
          'Jenjang:',
          ['SD', 'SMP', 'SMA'])
subdata = data[data["Jenjang"] == jenjang]

fig = px.line(subdata, "Tahun", "Persentase", 
              color = "Kelompok",
              color_discrete_sequence=["#DC1C13", "#EA4C46", "#F07470", "#F1959B", "#F6BDC0"],
              markers = True, 
              title = "Angka Tidak Sekolah Jenjang " + jenjang)

fig.update_xaxes(nticks=3, tickformat = '%Y')
fig.update_yaxes(tickformat = '.01%')

st.plotly_chart(fig, use_container_width=True)

st.subheader('Semakin Tinggi Jenjang Pendidikan, Semakin Banyak yang Tidak Bersekolah')

'''
Dapat dilihat bahwa persentase anak tidak sekolah untuk jenjang SD berada pada
rentang 0.3% hingga 1.6%, jenjang SMP berada pada rentang 3% hingga 12%, dan
jenjang SMA berada pada rentang 10% hingga 35%. Secara keseluruhan, semakin 
tinggi jenjang pendidikannya, semakin banyak anak yang tidak bersekolah. Hal 
ini mungkin disebabkan biaya sekolah yang semakin tinggi untuk jenjang yang 
semakin tinggi.
'''

st.subheader('Golongan Masyarakat Dengan Pendapatan Terendah Butuh Perhatian Khusus')

'''
Dari ketiga jenjang sekolah, dapat dilihat dengan jelas bahwa salah satu kelompok
masyarakat memiliki angka tidak sekolah yang tertinggi dibandingan dengan kelompok
lainnya, yaitu Kuintil 1. Kelompok ini merupakan kelompok masyarakat yang pendapatannya
kurang dari 20% di antara pendapatan terendah dengan pendapatan tertinggi. Sebagai
contoh, di antara sekelompok orang, pendapatan terendah adalah Rp100.000 dan
pendapatan tertinggi adalah Rp1.000.000. Jika pendapatan seseorang kurang dari
Rp200.000, ia termasuk ke dalam kelompok Kuintil 1. Jika pendapatannya di antara
Rp200.000 hingga Rp400.000, ia termasuk ke dalam kelompok Kuintil 2. Begitu pula
untuk seterusnya.
'''

'''
Masyarakat yang tergolong ke dalam Kuintil 1 ini masih perlu dibantu sehingga tidak
terjadi kejenjangan sosial di antara golongan yang lain. Pada saat persentase
anak tidak sekolah jenjang SD dari golongan lainnya berada di bawah 0.8%, 
persentase dari golongan Kuintil 1 masih berada di atas 1% selama 3 tahun terakhir.
Untuk jenjang SMP, persentase dari golongan Kuintil 1 berada di atas 10%, sedangkan
golongan lainnya berada di bawah 8% selama 3 tahun terakhir.
'''

st.subheader('Grafik yang Landai Di Tahun 2020-2021')

'''
Meskipun demikian, terdapat hal yang menarik dari angka tersebut di antara tahun
2020 dengan 2021. Pandemi Covid-19 yang seharusnya menyulitkan ekonomi masyarakat
justru tidak terlalu mempengaruhi angka anak yang tidak sekolah. Tabel di bawah ini
menunjukkan perbandingan rata-rata perubahan persentase untuk semua golongan 
(baik meningkat maupun menurun) untuk ketiga jenjang pendidikan.
'''

diff_19_20 = []
diff_20_21 = []
for jenjang in ['SD', 'SMP', 'SMA']:
  data_jenjang = data[data['Jenjang'] == jenjang]
  sum_diff = [0, 0]

  for kuintil in range(1,6):
    data_kuintil = data_jenjang[data_jenjang['Kelompok'] == 'Kuintil ' + str(kuintil)].reset_index(drop = True)
    sum_diff[0] += abs(data_kuintil['Persentase'][1] - data_kuintil['Persentase'][0])
    sum_diff[1] += abs(data_kuintil['Persentase'][2] - data_kuintil['Persentase'][1])

  diff_19_20.append(sum_diff[0] / 5)
  diff_20_21.append(sum_diff[1] / 5)

data_diff = pd.DataFrame({'Perubahan Persentase 2019-2020': diff_19_20,
                          'Perubahan Persentase 2020-2021': diff_20_21})
data_diff = data_diff.set_index([['SD', 'SMP', 'SMA']])

st.dataframe(data_diff)

'''
Dari tabel di atas, dapat dilihat bahwa perubahan persentase anak tidak sekolah
tidak berubah secara signifikan. Dibandingkan dengan perubahan persentase pada
tahun 2019-2022, perubahan persentase tahun 2020-2021 termasuk cukup kecil, kecuali
untuk jenjang SMP. Meskipun demikian, persentase untuk jenjang SMP cenderung menurun.
Hal ini dapat menjadi evaluasi bagi pemerintah untuk menyelidiki faktor-faktor
yang menyebabkan perubahan jumlah anak tidak sekolah tidak berubah terlalu signifikan
meskipun di tengah-tengah pandemi.
'''

st.header('Kesimpulan')

'''
Berdasarkan pemaparan yang sudah dituliskan, dapat disimpulkan bahwa perlu adanya
alokasi dana yang lebih pada sektor pendidikan khususnya untuk masyarakat golongan
Kuintil 1 untuk dapat mengurangi adanya kesenjangan sosial antar golongan. Selain itu,
pemerintah perlu menyelidiki kembali faktor apa saja yang mengakibatkan perubahan 
persentase anak tidak sekolah tidak berubah secara signifikan di tengah pandemi,
bahkan dapat menurunkan angka anak tidak sekolah. 
'''

st.header('Referensi')

'''
1. https://ekonomi.bisnis.com/read/20220904/44/1573854/resmi-naik-ini-daftar-terbaru-harga-bbm-pertamina-september-2022
2. https://indonesiabaik.id/videografis/alasan-harga-bbm-naik
3. https://www.cnbcindonesia.com/news/20220904094859-4-369108/sri-mulyani-ungkap-alasan-harga-bbm-naik-ini-hitungannya
4. https://www.cnnindonesia.com/nasional/20220623153552-25-812699/ri-ajak-g20-kuatkan-komitmen-pulihkan-learning-loss-dunia-pendidikan
5. https://www.bps.go.id/
'''
