''''
Diketahui:

1. Memiliki format: namaUser@namaHosting.ekstensi
2. namaUser hanya boleh terdiri atas huruf, angka, dash ('-') dan 
   underscore ('_').
3. namaHosting hanya boleh terdiri atas huruf dan angka.
4. ekstensi hanya boleh terdiri atas huruf, dengan 
   maksimum 5 karakter

Contoh:

✅ Alamat email valid:

lintangwisesa@ymail.com
lintang@purwadhika.com
lintang123@ironman123.space
❌ Alamat email tidak valid:

l/nt*ngw:s=s!@ym~il.com
lintang@purwadhika.community
lintang123@ironman123

'''
a = input('Input email: ')


def coba(a):
    a = a.replace('@', ' ')
    a = a.replace('.', ' ')
    a_split = a.split(' ')

    if len(a_split) != 3: 
        return 'Email tidak valid'
    else:
        nU = a_split[0]
        nH = a_split[1]
        tambahan = a_split[2]
        if tambahan.isalpha() == False or len(tambahan) > 5:
            return 'Email tidak valid'    
        else:
            if nH.isalnum() == True:
                if nU.isalnum() == True or '_' in nU or '-' in nU:
                    return 'Email calid'
                else:
                    return 'Email tidak valid'
            else:
                return 'Email tidak valid'
print(coba(a))