Ứng dụng Sao chép Cấu trúc Thư mục
Giới thiệu
Đây là một ứng dụng nhỏ gọn được xây dựng bằng Python và thư viện CustomTkinter. Chương trình cho phép người dùng chọn một thư mục nguồn và một thư mục đích, sau đó sao chép toàn bộ cấu trúc thư mục từ nguồn sang đích mà không sao chép các tệp tin bên trong.

Các tính năng nổi bật
Giao diện người dùng hiện đại: Sử dụng CustomTkinter để tạo các nút bo tròn và giao diện sạch sẽ, thân thiện.

Lưu đường dẫn tự động: Tự động lưu lại đường dẫn thư mục nguồn đã chọn từ phiên làm việc trước vào Windows Registry, giúp tiết kiệm thời gian cho lần sử dụng sau.

Tích hợp icon: Sử dụng tệp folder.ico làm icon cho chương trình, đảm bảo hiển thị chất lượng cao trên Windows.

Xử lý lỗi: Tích hợp các thông báo lỗi để cảnh báo người dùng khi chưa chọn đủ đường dẫn hoặc khi có lỗi xảy ra.

Yêu cầu hệ thống
Chương trình yêu cầu các thư viện Python sau:

customtkinter: Dùng để tạo giao diện người dùng.

pillow (PIL): Dùng để xử lý hình ảnh và tích hợp icon.

Bạn có thể cài đặt chúng bằng lệnh sau:

Bash

pip install customtkinter pillow
Hướng dẫn sử dụng
Chọn Thư mục Nguồn: Nhấn nút "Chọn thư mục nguồn" và chọn thư mục bạn muốn sao chép cấu trúc. Đường dẫn sẽ hiển thị ngay bên dưới nút.

Chọn Nơi Lưu: Nhấn nút "Chọn nơi lưu" và chọn thư mục đích. Đường dẫn sẽ hiển thị bên dưới nút.

Sao chép: Nhấn nút "Sao chép!" để bắt đầu quá trình.

Thông báo: Sau khi hoàn tất, một thông báo sẽ hiện lên. Nếu có lỗi, một hộp thoại lỗi sẽ cung cấp thông tin chi tiết.

Ghi chú về việc lưu đường dẫn
Chương trình sử dụng Windows Registry để lưu đường dẫn thư mục nguồn đã chọn. Điều này có nghĩa là bạn sẽ không thấy bất kỳ tệp tin nào được tạo ra trong thư mục dự án để lưu thông tin. Lần tới khi bạn mở chương trình, đường dẫn cuối cùng sẽ tự động được tải lên.

Hướng dẫn tạo file EXE
Để đóng gói chương trình thành một file .exe có thể chạy độc lập, bạn cần cài đặt PyInstaller.

Cài đặt PyInstaller:

Bash

pip install pyinstaller
Tạo file EXE: Đảm bảo tệp copy_folders.py và folder.ico nằm trong cùng một thư mục, sau đó chạy lệnh sau trong terminal:

Bash

pyinstaller --onefile --windowed --add-data "folder.ico;." --icon="folder.ico" copy_folders.py
--onefile: Gói tất cả vào một tệp duy nhất.

--windowed: Ứng dụng chạy không có cửa sổ terminal.

--add-data "folder.ico;.": Đính kèm file folder.ico vào gói.

--icon="folder.ico": Sử dụng file folder.ico làm icon cho file .exe.


Sau khi lệnh chạy thành công, file .exe sẽ nằm trong thư mục dist.
