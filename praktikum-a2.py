print ('praktikum-a2\n')

print ('NAMA    : INDRA WAHYULLA')
print ('NIM     : 231031017')
print ('PRODI   : SISTEM INFORMASI A\n')

# INI OPERATOR ASSIGNMENT
print ('Operator Assignment')
a = 19
print ('nilai a adalah',a)
a += 3
print ('nilai a+=3 adalah',a)

a = 19
print ('nilai a adalah',a)
a -= 3
print ('nilai a-=3 adalah',a)

a = 19
print ('nilai a adalah',a)
a *= 2
print ('nilai a*=3 adalah',a)

a = 19
print ('nilai a adalah',a)
a /= 2
print ('nilai a/r=3 adalah',a)

a = 3
print ('nilai a adalah',a)
a **= 2
print ('nilai a**=3 adalah',a)

a = 35
print ('nilai a adalah',a)
a %= 32
print ('nilai a%=32 adalah',a)

a = 35
print ('nilai a adalah',a)
a //= 32
print ('nilai a//=32 adalah',a)

# TUGAS MELANJUTKAN UNTUK OPERATOR SELANJUTNYA LINE 25 - LINE 59
print ('\nTugas Operator Assignment')
a = 35
print ('nilai a adalah',a)
a &= 32
print ('nilai a&=32 adalah',a)

a = 35
print ('nilai a adalah',a)
a |= 32
print ('nilai a|=32 adalah',a)

a = 35
print ('nilai a adalah',a)
a ^= 32
print ('nilai a^=32 adalah',a)

a = 35
print ('nilai a adalah',a)
a >>= 32
print ('nilai a> >=32 adalah',a)

a = 35
print ('nilai a adalah',a)
a <<= 32
print ('nilai a< <=32 adalah',a)

# OPERATOR PERBANDINGAN
print ('\nOperator Perbandingan')
a = 9
b = 13
print('----------- Besar dari 17 ----------')
hasil = a>17
print(a,'> 17 adalah',hasil)
hasil = b>17
print(b,'> 17 adalah',hasil)

print('\n----------- Kecil dari 17 ----------')
hasil = a<17
print(a,'< 17 adalah',hasil)
hasil = b<17
print(b,'< 17 adalah',hasil)

# TUGAS OPERATOR PERBANDINGAN 
print ('\nTugas Operator Perbandingan')
print('----------- Besar atau sama dari 17 ----------')
#>=
hasil = a>=17
print(a,'>= 17 adalah',hasil)
hasil = b>=17
print(b,'>=17 adalah',hasil)
print('\n----------- Kecil atau sama dari 17 ----------')
#<=
hasil = a<=17
print(a,'<= 17 adalah',hasil)
hasil = b<=17
print(b,'<= 17 adalah',hasil)
print('\n----------- Sama dari 17 ----------')
#==
hasil = a==17
print(a,'== 17 adalah',hasil)
hasil = b==17
print(b,'== 17 adalah',hasil)
print('\n----------- Tidak Sama dari 17 ----------')
#!=
hasil = a!=17
print(a,'!= 17 adalah',hasil)
hasil = b!=17
print(b,'!= 17 adalah',hasil)

#Operator logika
print ('\nOperator Logika')
a = True
b = False

print ('========== AND ==========')
hasil = a and a
print(a,'and',a,'hasilnya =',hasil)

hasil = a and b
print(a,'and',b,'hasilnya =',hasil)

hasil = b and a
print(b,'and',a,'hasilnya =',hasil)

hasil = b and b
print(b,'and',b,'hasilnya =',hasil)

print ('\n========== OR TUGAS ==========')
hasil = a or a
print(a,'and',a,'hasilnya =',hasil)

hasil = a or b
print(a,'and',b,'hasilnya =',hasil)

hasil = b or a
print(b,'and',a,'hasilnya =',hasil)

hasil = b or b
print(b,'and',b,'hasilnya =',hasil)


print ('\n========== XOR ==========')
hasil = a ^ a
print(a,'xor',a,'hasilnya =',hasil)

hasil = a ^ b
print(a,'xor',b,'hasilnya =',hasil)

hasil = b ^ a
print(b,'xor',a,'hasilnya =',hasil)

hasil = b ^ b
print(b,'xor',b,'hasilnya =',hasil)

print ('\n========== NOT ==========')
hasil = not a
print('not',a,'hasilnya =',hasil)

hasil = not b
print('not',b,'hasilnya =',hasil)

#OPERATOR MEMBERSHIP
print ('\nOperetor Membership')
print ('========== IN ==========')
nama = 'indra'

test = 'in'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test = 'ni'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'
cek = test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)
cek = test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)
cek = test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)
cek = test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)
cek = test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)

print ('\n Tugas Operetor Membership')
print ('========== NOT IN ==========')
nama = 'indra'

test = 'in'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah',cek)

test = 'ni'
cek = test not in nama
print(test,'tidak terdapat di',nama,'adalah',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'
cek = test1 not in nama
print(test1,'tidak terdapat di',nama,'adalah',cek)
cek = test2 not in nama
print(test2,'tidak terdapat di',nama,'adalah',cek)
cek = test3 not in nama
print(test3,'tidak terdapat di',nama,'adalah',cek)
cek = test4 not in nama
print(test4,'tidak terdapat di',nama,'adalah',cek)
cek = test5 not in nama
print(test5,'tidak terdapat di',nama,'adalah',cek)