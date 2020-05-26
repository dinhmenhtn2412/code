import sqlite3
"""db= sqlite3.connect("school.sql")
db.execute("DROP TABLE IF EXISTS student")
db.execute("CREATE TABLE student ( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR NOT NULL)")
db.execute(" INSERT INTO student(name) VALUES ('Duong Van Dinh')")
db.execute(" INSERT INTO student(name) VALUES ('Nguyen Van Nghiep')")
db.execute(" INSERT INTO student(name) VALUES ('Nguyen The Anh')")
db.execute(" INSERT INTO student(name) VALUES ('Nguyen Hai Nam')")
db.commit()
db.execute("UPDATE student SET name=\"Ngyen Hong Hoan\" WHERE id = 1")
results=db.execute("SELECT * FROM student")
for row in results:
	print(row)"""

Db= sqlite3.connect("Banhang.sql")
Db.execute("drop table if exists SanPham")
Db.execute("CREATE TABLE SanPham (id Interger primary Key not null, Ten nvarchar(50) not null, Gia real not null)")
Db.execute("Insert Into SanPham(id, Ten, Gia) values (1,'Laptop',1000)")
Db.execute("Insert into SanPham(id, Ten, Gia) values (2,'PC',1300)")

readDB=Db.execute("Select Ten from SanPham")
a=[]
for item in readDB:
    a.append(item)
print(a)