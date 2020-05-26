def DienThoai(**Data):
    count=0
    for name, price in Data.items():
        row="{:10}{:10}".format(name, price)
        print(row)
        count+=10
    return count
print('{:-^30}'.format("BANG GIA DIEN THOAI"))
a={'Samsung':5000, 'Apple':5100, 'Huaweit':4900}
c=DienThoai(Oppo=4500, Xiaomi=4000, SamSung=5000, Apple=5200)
print("-"*25)
print("{:10}{:10}".format("Tong:",c))
