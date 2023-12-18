
print('\n')
biodata = { 'nama'  : 'Fikri Fauzan Pratama',
'nim'   : '231031103',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'Parepare,17 februari 2004',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'alamat': 'jalan bambu runcing btn anugrah no.1',
'email' : 'ramef814@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)




