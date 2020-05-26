           CÁC HÀM VÀ CẤU TRÚC TRONG PYTHON

1. Các hàm cơ bản
	3**100 = 3^100 lũy thừa
	min(1,2,3,4)= 1 
	max(12,3,4)= 4
	abs(-115) = 115  Hàm gia trị tuyệt đối
	round(a, n): Làm tròn số 'a' tới 'n' chữ số thập phân.
	x.append(a) thềm phần tử a vào list x
	range(x) : tạo dãy số x phần tử
	range(x,y) : tạo dãy số từ x tới y
	range(x,y,z): tạo dãy số từ x tới y bước nhảy z


Hàm toán học
	Để sử dụng cần khai báo thư viện: import math

	math.sqrt() : hàm giá trị tuyệt đối.
	math.fatorial(): hàm giai thừa
	math.cell(): làm tròn lên
	math.floor(): làm tròn xuống

bolean: e=10>6 true
		e=10<6 fall
2. Kiểu str
	Để viết được dấu " cần có một dấu ' \' ở phía trước."
Một số kiểu cơ bản:
	tuple ví dụ như: tup=(1,2,3,4,5) hoặc tupl=("duong","van","dinh")
 	list vì dụ: list=[1,2,3,4,5]
 	set ví dụ: se={3,2,4} có thể có cả chữ và số
 	dict ví dụ : t={'n1':'duong','n2':'van','n3':'dinh'}

Các toán tử gán trong python bạn có thể xem ở bài 7
	x<<=3 là x=x*3*3
	x>>=3 là x=x/3/3
	x//3 là x chia cho 3 và làm tròn xuống
Mệnh đề điều kiện if, 'while' and foR (chi tiết xem bài 8)
   cách sử dụng continue và break giống với lập trình C
3. Chapter 3
	len(x) là lệnh để lấy chiều dài của chuỗi
	x[4] lấy phần tử ở vị trí số 4 trong chuỗi x.
		x[-4] lấy phần tử ở vị trí số 4 từ cuối lên
		x[y:z] lấy từ vị trí y đến z
		x[y:] lấy từ vị trí y tới hết
		x[:y] lấy từ đầu đến vị trí y
	x.capitalize()viết hoa chữ cái đầu tiên trong xâu x
	x.upper() viết hoa toàn bộ sâu x
	x.lower() viết thường xâu
	x.swapcase()  hàm đổi chữ thường thành chữ hoa và ngược lại
	x.ljust(10,"*") hàm thêm n ký tự * vào phía sau để chuỗi có 10 ký tự
	x.rjust(10,"*") vào trc
	x.center(10,"*") thêm ký tự * vào hai đầu
	x.lstrip() xóa khoảng trắng bên trái xâu
	x.rstrip() xóa khoảng trắng bên phải xâu
	x.strip() xóa khoảng trắng ở cả hai bên
	x.strip("*") xóa ký tự * khỏi xâu
	x.find("duong") tìm vị trí của từ duong trong xâu, nếu không có
sẽ trả về -1
	x.find("dinh",5) tìm vị trí từ đinh từ vị trí số 5 trở đi
	x.find("dinh",5,30) tìm vị trí từ dinh from 5 to 30
	z.index("duong van") tìm vị trí từ duong van trong xau x
	x.replace("Duong","Nguyen") sửa từ Duong thanh Nguyen
	x.isalnum() trả về giá trị true nếu chuỗi có ít nhất một ký tự
 a to z chữ số và không có khoảng trắngm không có ký tự đặc biệt
 	x.isalpha() test chuỗi chỉ gồm ký tự a to z
 	x.isdigit() test chuỗi chỉ gồm kí tự số
 	x.isspace() test chuỗi chỉ gồm khoảng trắng
 	s.split() cắt chuỗi s theo khoảng trắng thành list
 		s.split('x') cắt dựa vào ký tự x
 gộp list thành chuỗi ta dùng: k.join(l) trong đó: k=" " và l là một list 

FORMAT
	p=" Duong van Dinh {} tuoi".format("19") thay số 19 vào {}
	date=("24","12","2000")
	pr=" Sinh ngay{0} thang{1} nam {2}",format(*date) :thay lần lượt vị trí
	a='{:x<20}'.format("dinh") thêm vào bên phải ký tự x cho đủ 20
	a='{:x>20}'.format("dinh") trái
	a='{:x^20}'.format("dinh") thêm vào hai bên
	p="So thu tu: {0:d}".format(24) chỉ có thể chuyền vào số,hexa s, 
		nhị phân b ,o
4. Chapter 4 list
	len(x) lấy chiều dài của x
	x[4] lấy phần tử ở vị trí số 4
	x[-4] lấy từ phải qua trái các hàm ở đây giống với str
	c=x+[x[4]+1] bạn thêm phần tử x[4]+1 vào list x
	x.append(11) thêm số 11 vào list x
	x.insert(4,5) thêm số 5 vào vị trí 4
	x.pop(5) xóa phần tử ở vị trí 5
	x.count(3) đếm số lần xuất hiện của só 3
	x.sort() sắp xếp lại list
	del x[0:3]
	x[0]=3  thay phần tử x[0] bằng 3
xem cách viết tắt và gọn ở bài 21
5. Chapter 5
tuple bạn có thể dùng từ cuối lên vd: x[-5,-1]
các câu lệnh tương tự với list, đặc biệt nó có thể cộng tuple
set khác với tuple và list
bạn có thể cộng hai set với nhau, A,b : cộng A với 
	A-B : loại bỏ những phẩn tử trong A mà B có
	A|B : Gộp lại và loại bỏ phần tử đã có ở A
	A&B : Giữ lại phần tử chung của hai set
	A^B : Xóa phần tử chung rồi gộp lại  
dict: 
	len(x) độ dài x
		x['key']: lấy phần tử key
	không cho phép cộng
	del x['key'] xóa phần tử k
	x.values() lấy values của dict x
	x.keys() lấy key của dict x
	x=dict(a=10,b=11,c=12) tạp thành dict tương ứng
	x['key']='dinh' thay phan tu x['key']
	'key' in d là hàm true false
	x.pop('key') xóa phần tử key
	x.popitem() xóa ngẫu nhiên phần tử trong x
	d['Key']='khóa'  Đổi phần từ "Key" "thành khóa"
6.Chapter 6 hàm trong python
	def name(): 
		code
		return("x")
	cách dùng : name(x) x là tham số nếu có
	return() dùng để trả về biến nếu cần
	nếu có tham số mặc định thì bạn phải gán từ phải sang trái
	nếu như cần truyền nhiều:
		def name(*data)
		vòng for với list thì có teenlist.items()
	cách dùng iter tương tự như for, nó sẽ lấy từng phần tử một
		x=name.iter()
		x.__next__()
	yield cách dùng giống với return tuy nhiên có thể trả về nhiều
lần trong một vòng for
7.Chapter7 clasS
 khi dùng deF bắt buộc phải có (self)
 constructor: deF __init__ là tự động in (bai 37)
 			lưu ý trong init không được sử dụng return
 		__str__ có thể dùng return

 KẾ THỪA:
 class Name (nguoi)  Kế thừa các thuộc tính của lớp người
8. Chapter 8  Thao tác với file trong python
	
	f=open("file.txt","r")  mở file để: r, w
	f.close()  đóng file
	for line in f:
		f.write(" ghi vào file f")
	trong trường hợp file lớn, cần đọc file theo cách sau:
		 #xem trong bài 43 
		 BUFFERSIZE=10000
		 buffer=rfile.read(BUFFERSIZE)
		 ghi: 
		 while (len(buffer)>0):
		 	wfile.wirte(buffer)
		fpos=f.tell()  xem file đã chạy tới đâu
		f.seek(vt)    đọc file f từ vị trí vt
	cách dùng module:
		import random as ra
		mỗi một module có cách dùng khác nhau
9. Chapter 9 module trong PYTHON
	có các loại module có sẵn hoặc các module tự viết
10. Chapter 10

 try:
 	a=100
 	b=0
 	x=a/b
 except ZeroDivisionError as error:
 	print("loi: ",error)
11. 
 các câu lệnh sql cơ bản:

 CREATE TABLE "mon hoc"("id" INTEGER PRIMARY KEY
 	AUTOINCREMENT NOT NULL,"name"VARCHAR NOT NULL)

 xóa bảng: DROP TABLE "main"."monhoc"
 
 chèn: INSERT INTO monhoc(name) VALUES("Toan")
 update: UPDATE monhoc SET name="Ngu van" WHERE id = 1
 xóa : DELETE FROM mon hoc WHERE id=2
 chọn bảng: SELECT*FROM monhoc
 			SELECT name FROM monhoc 
 			SELECT*FROM monhoc WHERE id=3
 			SELECT*FROM monhoc ORDER by id DESC/ASC
 			SELECT*FROM monhoc LIMIT(1,2) từ dòng hai lấy 2 ký tự
12 array ( mảng trong python)
 import array as np 
 	a=arr.array('i',[11,2,3,4,5])
 		là khai báo mảng i kiểu int, 'l' long int
 	bạn có thể in chuỗi phần tử trong mảng bằng cách:
 	b=arr.array('i',a)
 	print(a[0:4])
 	thay đổi một phần tử: a[0]=10
 	thay đổi nhiều: a[0:3]=arr.array('i',[1,3,5,7])
 	hai mảng cũng có thể nối lại thành toán tử:
 	 b=arr.array('i',array)
 	 tạo mảng trống c=arr.array('i')
 	 ghép 2 mảng: c=a+b #done
 	 del a[2]  xóa phần tử thứ 3.
 	 a.remove(1)
 	 print(a.pop(1))

 	Thư viện numpy :
 	import numpy as np
 	mangA=np.array([2,3,4,5,6,8])
 	mangB=np.arange(25) #tạo một mảng có 25 ptử
 	mangB.reshape(5,5) #tạo mảng 5 5, ma trận
 	mang=np.arange(25).reshape(5,5)

 	 ví dụ:
 	 	abc=np.array([[1,2,3,4,5,6],[1,2,4,67,8,8]])
 	 	abc.shape ==>> output is (2,6)
 	Tạo một mảng chứa 5 ptu 0:
 			np.zeros(5)
 			np.ones(10) #tạo 10 phẩn tử có gt 1.
 			np.twos(5)
 			np.zeros(2,1) #tạo mảng 0 hình 2 dòng một ô.
 	+array arithmetic
 		arr + 10 #thêm vào mỗi phần tử 10 đơn vị
 		arr*arr #nhân mỗi phần tử với chính nó
 		arr**2 # mỗi phần tử lũy thừa 2
 		name.T # đổi dòng thành cột, và ngược lại
 	a1=a[:10] # lấy 10 ptu cua a ve a1
 	a1[:100]#chuyển ptu cua a1 thanh 100
 	#khi in a van bao gom ca a1
 	a1[0]=100 đổi ptu
 	b=a.copy()

 	xem thêm bài 61
 		for i in range(10):
			x.append(np.random.randint(1,10))

 	np.add(x,y) #cộng phần tử tương ứng của hai mảng x, y
 	np.maxium(x,y) # lấy phần tử lớn hơn tương ứng 2 mảng
 	np.minium(x,y)
 	np.sqrt(x) #lấy căn bặc 2.
 	np.square(x)#lấy mũ 2
 	np.device(x,y)# lấy mảng x chia cho mảng y
 	np.power(x,y) # lấy lũy thừa của x bậc y tương ứng
 	x.sort() #sắp xếp mảng x theo thứ tự tăng dần
 	np.unique(x) # loại bỏ những phần tử trùng trong x
 	np.greater(x,y) #so sánh các phần tử tương ứng của x> y;

 	b=np.greater(x,y)
 		b.all()# tất cả p tử đều đúng, nếu sai >>> false
 		b.any()# bất kì p tử đúng  nếu có >>> true
 	google seach: python numpy function# thêm thông tin
 13. Chapter 13 pandas series
 	- xem bài 64/
 	ind="a b c d e f g h".split()#tách phẩn tử theo khoảng trắng
		thành: ['a','b'...]	

	df1=pd.read_clipbroad()#chèn một băng tử clipbroad
	chi tiết thêm xem bài 70 và 71 thanks
	df1.sum() #tính tổng các cột
	df1.sum(axis=1)# tính tổng các hàng
	df1.max() # trả về giá trị mã của mỗi cột
	nd=np.na 

	
	






 			
















	 



 



	


