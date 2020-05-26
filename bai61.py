import numpy as np
A=np.range(25).reshape(5,5)
print(A[0])     #in ra hàng dầu tiên
A[2][2] phần tử ở hàng 2 cột 2
A[2:4] #chọn hàng từ 2 đến <4
A[2:4,1:4] #chọm phần từ 2 <4 và cột 1<4
A[1,2,4]  #chọn 3 hàng 1,2,4
A.sum() #tính tổng mảng
