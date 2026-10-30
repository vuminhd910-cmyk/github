# Bước 1 import class fast api từ thư viện 
from fastapi import FastAPI
from pydantic import BaseModel

class student(BaseModel):
    id: int
    name: str
    age: int


app = FastAPI(
    title = "Đây là API của CNTT2",
    description = "Hú hú "
) 

# bước 3 định nghĩa đường dẫn gốc "/" bằng phương thức GET (HTTP method)
@app.get("/")
def get_root():
    # hàm trả về một dictionary, Fast API sẽ tự chuyển đổi thành dạng json 
    return {
        "message": "Hello MINHDUC DEP ZAI" 
    }

# định nghĩa các routing cho API theo chuẩn của RestFul 
# get 
# lấy danh sách toàn bộ sinh viên 
@app.get("/students")
def get_students():
    print("Lấy danh sách sinh viên")

    return [{"id": 1, "name": "Nguyễn Văn A"}]  
# post tạo sinh viên mới
@app.post("/students")
def create_student():
    print("thêm mới sinh viên")

    return {
        "message" :"Thêm mới thành công"
    }
# put : cập nhật toàn bộ thông tin sinh viên theo ID 
@app.put("/students/{student_id}")
def update_student(student_id: int):
    print(f"cập nhật sinh viên có id là: {student_id} ")

    return {
        "message": "đã cập nhật thành công sinh viên có id: {student_id}"
    }

# patch - cập nhật một phần nhỏ thông tin của sinh viên 
@app.patch("/students/(student_id)")
def patch_student(student_id: int):
    print(f"đã cập nhật một phần dữ liệu của {student_id}") 
    return {
        "message":"Đã cập nhật thành công sinh viên"
    }

# delete xóa vĩnh viễn thông tin của sinh viên theo ID 
@app.delete("/students/{student_id: int}")
def delete_student(student_id: int):
    print("Xóa thành công sinh viên có id là student ")
  
    return {
        "message":"Đã xóa thành công sinh viên"
    }
""" 
1. path parameter 
đường dẫn có tham số 
2. query parameter 
truy vấn có tham só 
3. request body 
4. type hints
""" 
@app.get("/students")
def get_students():
   
@app.get("/student/{student_id:int}"):
def get_student_dtetail():
    # trả về thông tin chi tiết của sunh viên 
    for student in students ;
        if student["id"] == student_id:
            return{
                "message": "lấy chi tiết sinh viên thành công",
                "data": student
            }
            ]
            ]
@app.post("/students")
def create_student(student:student):
    new_student ={
        "id":student.id,
        "name":student.id,
        "age":student.age
    }

    print("Thông tin sinh viên cần thêm", new_student) 
