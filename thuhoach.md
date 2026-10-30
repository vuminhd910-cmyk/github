# BÀI THU HOẠCH: TÌM HIỂU TỔNG QUAN VỀ WEB BACKEND VÀ FASTAPI

## Phần 1: Khái niệm cơ bản

### 1. Backend là gì?

Nếu coi một trang web như một nhà hàng, thì Frontend là không gian quán, bàn ghế và thực đơn – những gì khách hàng (người dùng) nhìn thấy và tương tác trực tiếp. Còn **Backend chính là khu vực nhà bếp**.

* Backend là phần chạy ngầm ở phía máy chủ (Server), người dùng không thể nhìn thấy trực tiếp.
* Nhiệm vụ chính của Backend là xử lý các logic nghiệp vụ, tính toán, và quản lý dữ liệu (như lưu trữ tài khoản, xử lý đơn hàng, bảo mật thông tin).

### 2. Mô hình Client – Server là gì?

Đây là mô hình giao tiếp cơ bản nhất trên Internet giữa hai bên:

* Client (Máy khách): Là thiết bị hoặc ứng dụng phía người dùng (như trình duyệt Chrome trên máy tính, app Facebook trên điện thoại) gửi yêu cầu (Request) đi.
* Server (Máy chủ): Là một máy tính có cấu hình mạnh, hoạt động 24/7, nằm ở đâu đó trên mạng. Server nhận yêu cầu từ Client, xử lý rồi trả về kết quả (Response).

> *Ví dụ:* Khi bạn lướt TikTok, điện thoại của bạn là Client gửi yêu cầu "xem video tiếp theo", hệ thống máy chủ của TikTok là Server sẽ gửi video đó về cho bạn xem.

### 3. API là gì?

API (Application Programming Interface) đóng vai trò như **một người phục vụ bàn** trong nhà hàng.

* Nó là cầu nối trung gian cho phép hai ứng dụng hoặc thành phần (ví dụ như Client và Server) nói chuyện và trao đổi dữ liệu với nhau.
* Khi Client muốn lấy dữ liệu từ Server, nó không thể tự tiện vào kho dữ liệu mà phải thông qua API. API sẽ cầm yêu cầu đó vào Server lấy đúng thứ Client cần và mang ra ngoài.

### 4. JSON là gì?

JSON (JavaScript Object Notation) là một **định dạng chuẩn dùng để đóng gói dữ liệu dưới dạng văn bản**. Nó có cấu trúc gồm các cặp `khóa: giá trị` (key: value) rất gọn gàng và dễ nhìn.

* Vì các hệ thống khác nhau (như Python, Java, JavaScript) có cách hiểu dữ liệu khác nhau, nên chúng cần một "ngôn ngữ chung" để giao tiếp. JSON chính là ngôn ngữ chung đó vì cả người và máy tính đều đọc hiểu rất dễ dàng.


## Phần 2: Kiến thức Web cơ bản

### 1. HTTP là gì?

HTTP (Hypertext Transfer Protocol) là **bộ quy tắc (giao thức) truyền tải dữ liệu** trên mạng Internet. Bạn có thể hiểu nó như "luật giao thông" dành cho dữ liệu. Khi Client và Server muốn nói chuyện với nhau, cả hai bắt buộc phải tuân theo các quy tắc của HTTP để đảm bảo thông tin gửi đi và nhận lại không bị lỗi hoặc hiểu sai.

### 2. Các phương thức HTTP (GET, POST, PUT, DELETE)

Trong thế giới Web, bốn phương thức này tương ứng với các hành động cơ bản khi thao tác với dữ liệu (thường gọi là CRUD):

* **GET (Lấy dữ liệu):** Dùng khi Client muốn yêu cầu Server gửi thông tin về để xem. (Ví dụ: Bạn vào trang cá nhân để đọc bài viết).
* **POST (Tạo mới dữ liệu):** Dùng khi Client muốn gửi dữ liệu mới lên Server để lưu trữ. (Ví dụ: Bạn bấm nút "Đăng bài" hoặc điền form đăng ký tài khoản).
* **PUT (Cập nhật dữ liệu):** Dùng khi bạn muốn thay đổi, sửa đổi thông tin đã có sẵn trên Server. (Ví dụ: Bạn sửa lại nội dung một bài viết đã đăng hoặc đổi avatar).
* **DELETE (Xóa dữ liệu):** Dùng khi muốn gỡ bỏ hoàn toàn một thông tin nào đó khỏi hệ thống. (Ví dụ: Bạn bấm xóa một bức ảnh cũ).


## Phần 3: Tìm hiểu FastAPI

### 1. FastAPI là gì?

FastAPI là một **Web Framework mã nguồn mở hiện đại, được viết bằng ngôn ngữ Python** dùng để xây dựng các API. Đúng như cái tên "Fast", điểm đặc trưng lớn nhất của nó là tốc độ thực thi cực kỳ nhanh (ngang ngửa với các framework của Node.js hay Go) và giúp lập trình viên viết code nhanh hơn, ít lỗi hơn nhờ tận dụng các tính năng mới của Python.

### 2. FastAPI dùng để làm gì?

FastAPI được sử dụng chủ yếu để:

* Xây dựng phần Backend, làm hệ thống API cốt lõi cho các ứng dụng web và di động.
* Làm cổng kết nối và xử lý dữ liệu cho các ứng dụng Trí tuệ nhân tạo (AI) và Học máy (Machine Learning) – vì các mô hình này chủ yếu viết bằng Python, kết hợp với FastAPI sẽ cực kỳ mượt mà.
* Tự động tạo trang tài liệu (Documentation) cho API một cách trực quan để các lập trình viên Frontend nhìn vào là biết cách kết nối ngay.



## Phần 3: Tư duy hệ thống (Sơ đồ luồng hoạt động)

Để bạn dễ hình dung cách các thành phần này kết hợp với nhau, hãy tưởng tượng luồng đi của một hành động **"Đăng nhập tài khoản"** như sau:

```
[ Người dùng ]
      │
      ▼ (Nhập username/password)
[ Client: Trình duyệt Web ]
      │
      ▼ 1. Gửi HTTP POST request (chứa data dạng JSON) qua API
[ Server Backend: FastAPI ]
      │
      ▼ 2. Kiểm tra logic & Đọc/Ghi dữ liệu
[ Database: Cơ sở dữ liệu ]
      │
      ▲ 3. Trả kết quả xác thực thành công
[ Server Backend: FastAPI ]
      │
      ▲ 4. Trả về HTTP Response (JSON: "Đăng nhập thành công")
[ Client: Trình duyệt Web ]
      │
      ▼ (Hiển thị màn hình chính)
[ Người dùng ]



