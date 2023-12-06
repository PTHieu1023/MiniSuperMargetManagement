# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from UI_Forms.ui_py.manager_screen import Ui_MiniSuperMarketManagement

import psycopg2
import config

class MiniSuperMarketManagement(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MiniSuperMarketManagement()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MiniSuperMarketManagement()
    widget.show()
    sys.exit(app.exec())







    # conn_string = f"dbname={config.DATABASE['NAME']} user={config.DATABASE['USER']} password={config.DATABASE['PASSWORD']} host={config.DATABASE['HOST']} port={config.DATABASE['PORT']}"
    #
    # # Kết nối đến PostgreSQL
    # try:
    #     connection = psycopg2.connect(conn_string)
    #     print("Kết nối thành công!")
    #     cursor = connection.cursor()
    #
    #     # Chuỗi truy vấn SELECT
    #     select_query = "SELECT * FROM public.orders"
    #
    #     # Thực hiện truy vấn
    #     cursor.execute(select_query)
    #
    #     # Lấy kết quả truy vấn
    #     records = cursor.fetchall()
    #
    #     # In kết quả
    #     for row in records:
    #         print(row)
    #     column_names = [desc[0] for desc in cursor.description]
    #
    #     # Print column names
    #     print("Columns:")
    #     for col in column_names:
    #         print(col)
    #
    # except Exception as e:
    #     print(f"Lỗi kết nối: {e}")
    #
    # finally:
    #     # Đóng kết nối sau khi sử dụng
    #     if connection:
    #         connection.close()
    #         print("Kết nối đã đóng.")
