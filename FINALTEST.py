class HouseholdBill:
    def __init__(self,id,owner_name,address,electric_usage,electric_price,water_usage,water_price,service_fee):
        self.id = id
        self.owner_name = owner_name
        self.address = address
        self.electric_usage = electric_usage
        self.electric_price = electric_price
        self.water_usage = water_usage
        self.water_price = water_price
        self.service_fee = service_fee

        self.total_bill = 0
        self.bill_type = ""

        self.calculate_total_bill()
        self.classify_bill() 

    def calculate_total_bill(self):
        self.total_bill = (self.electric_usage * self.electric_price) + (self.water_usage * self.water_price) + self.service_fee
    def classify_bill(self):
        if self.total_bill >= 3000000 :
            self.bill_type = "Rất cao"
        elif self.total_bill >= 1500000 and self.total_bill < 3000000:
            self.bill_type = "Cao"
        elif self.total_bill >= 500000 and self.total_bill < 1500000:
            self.bill_type = "Trung bình"
        else:
            self.bill_type = "Thấp"


class HouseholdBillManager:
    def __init__(self):
        self.bills = []
    def show_all(self):
        if not self.bills:
            print("Hóa đơn hiện tại đang trống")
            return 
        for bill in self.bills:
            print(f"{bill.id:<10} | {bill.owner_name:<20} | {bill.address:<10} | {bill.electric_usage:<10} | {bill.electric_price:<10} | {bill.water_usage:<10} | {bill.water_price:<10} | {bill.service_fee:<10} | {bill.total_bill:<10} | {bill.bill_type}")
    
    def _validate_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print(" Lỗi: Số liệu phải là số nguyên lớn hơn hoặc bằng 0!")
                    continue
                return value
            except ValueError:
                print(" Lỗi: Vui lòng nhập một số nguyên hợp lệ!") 

    def add_bill(self):
        while True:
            id = input("Nhập vào mã hộ gia đình: ").strip().upper()
            if not id :
                print("Mã hộ gia đình không được để trống")
                continue
            if any(bill.id == id for bill in self.bills):
                print("Mã hộ gia đình không được trùng")
                continue 
            break 
        while True:
            owner_name = input("Nhập tên chủ hộ: ").strip()
            if not owner_name:
                print("Tên chủ hộ không được để trống")
                continue
            break 
        while True:
            address = input("Nhập địa chỉ chủ hộ: ").strip()
            if not address:
                print("Địa chỉ không được rỗng")
                continue
            break 
        electric_usage = self._validate_int("Nhập vào số điện sử dụng: ")
        electric_price = self._validate_int("Nhập vào đơn giá điện sử dụng: ")
        water_usage = self._validate_int("Nhập vào số nước sử dụng: ")
        water_price = self._validate_int("Nhập vào đơn giá nước: ")
        service_fee = self._validate_int("Nhập vào phí dịch vụ")

        new_bill = HouseholdBill(id,owner_name,address,electric_usage,electric_price,water_usage,water_price,service_fee)        
        self.bills.append(new_bill)

        print("Đã thêm hóa đơn mới thành công") 

    def update_bill(self):
        id = input("Nhập mã hộ gia đình cần cập nhật: ").strip().upper()
        found_id = None 
        for bill in self.bills:
            if bill.id == id:
                found_id = bill 
                break 
        if not found_id:
            print("Mã hộ gia đình không tồn tại ")
            return 
        electric_usage = self._validate_int("Nhập vào số điện sử dụng: ")
        electric_price = self._validate_int("Nhập vào đơn giá điện sử dụng: ")
        water_usage = self._validate_int("Nhập vào số nước sử dụng: ")
        water_price = self._validate_int("Nhập vào đơn giá nước: ")
        service_fee = self._validate_int("Nhập vào phí dịch vụ") 

        found_id.electric_usage = electric_usage 
        found_id.electric_price = electric_price
        found_id.water_usage = water_usage
        found_id.water_price = water_price
        found_id.service_fee = service_fee

        found_id.calculate_total_bill() 
        found_id.classify_bill()  
        
        print("Cập nhật thành công")


    def delete_bill(self):
        id = input("Nhập mã hộ gia đình có hóa đơn cần xóa: ").strip().upper()
        found_id = None 
        for bill in self.bills:
            if bill.id == id:
                found_id = bill 
                break 
        if not found_id:
            print("Mã hộ gia đình không tồn tại ")
            return  
        confirm_delete = input("Bạn có chắc muốn xóa hóa đơn này không(Y/N): ").strip().upper()
        if confirm_delete == "Y":
            self.bills.remove(found_id)
            print("Đã xóa thành công")
        else:
            print("Hủy bỏ thao tác xóa") 


    def search_bill(self):
        print("\n--- TÌM KIẾM HÓA ĐƠN ---")
        keyword = input("Nhập tên chủ hộ cần tìm (tìm kiếm gần đúng): ").strip().lower()

        if not keyword:
            print(" Lỗi: Từ khóa tìm kiếm không được để trống!")
            return

        results = [bill for bill in self.bills if keyword in bill.owner_name.lower()] 

        if not results:
            print(" Không tìm thấy hóa đơn phù hợp.")
            return

        print(f"\n🔍 Tìm thấy {len(results)} kết quả phù hợp:")
        for bill in results:
            row = (f"{bill.id:<10} | {bill.owner_name:<20} | {bill.address:<10} | {bill.electric_usage:<10} | {bill.electric_price:<10} | {bill.water_usage:<10} | {bill.water_price:<10} | {bill.service_fee:<10} | {bill.total_bill:<10} | {bill.bill_type}") 
            print(row) 


def main():
    manager = HouseholdBillManager()  
    
    manager.bills.append(HouseholdBill("H001","Vũ Minh Đức","Hà Nội",40,3000,50,3000,30000))
    manager.bills.append(HouseholdBill("H002","Vũ Minh Trang","Hà Nội",60,4000,100,4000,50000))
    manager.bills.append(HouseholdBill("H003","Nguyễn Lê Linh Chi","Hà Nội",70,5000,80,5000,60000)) 
    
    while True:
        print("\n================ HÓA ĐƠN TIỀN ĐIỆN NƯỚC ================")
        print("1. Hiển thị danh sách hóa đơn điện nước")
        print("2. Thêm hóa đơn điện nước mới")
        print("3. Cập nhật hóa đơn điện nước")
        print("4. Xóa hóa đơn điện nước")
        print("5. Tìm kiếm hóa đơn")
        print("6. Thoát hệ thống")
        print("=====================================================")
        
        choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
        if not choice:
            print("không được nhập lựa chọn rỗng")
            continue 
    
        match choice:
            case "1":
                print("Hiển thị danh sách hóa đơn")
                manager.show_all() 
            case "2":
                print("Thêm hóa đơn điện nước mới")
                manager.add_bill() 
            case "3":
                print("Cập nhật hóa đơn điện nước")
                manager.update_bill()
            case "4":
                print("Xóa hóa đơn điện nước")
                manager.delete_bill() 
            case "5":
                print("Tìm kiếm hóa đơn điện nước")
                manager.search_bill() 
            case "6":
                print("Thoát chương trình xin chào và hẹn gặp lại")
                break 
            case _:
                print("Hãy nhập lại lựa chọn của bạn nằm ngoài phạm vi của hệ thống")
            
if __name__ == "__main__":
    main() 




  