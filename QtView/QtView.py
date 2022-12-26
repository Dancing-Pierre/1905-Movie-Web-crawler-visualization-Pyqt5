import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QComboBox, QTableWidgetItem, \
    QLabel, QHBoxLayout
import pymysql


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("显示大屏")
        self.resize(800, 600)
        # 垂直布局按照从上到下的顺序进行添加按钮部件。
        vlayout = QVBoxLayout()
        y = QHBoxLayout()
        # 创建表格
        self.table = QTableWidget(0, 0)
        # 创建可视化图展示区域
        self.pixmap0 = QPixmap('')
        self.pixmap1 = QPixmap('IMG/dongzuo1.png')
        self.pixmap2 = QPixmap('IMG/dongzuo2.png')
        self.pixmap3 = QPixmap('IMG/aiqing1.png')
        self.pixmap4 = QPixmap('IMG/aiqing2.png')
        self.pixmap5 = QPixmap('IMG/lishi1.png')
        self.pixmap6 = QPixmap('IMG/lishi2.png')
        self.pixmap7 = QPixmap('IMG/neidi1.png')
        self.pixmap8 = QPixmap('IMG/neidi2.png')
        self.pixmap9 = QPixmap('IMG/jiating1.png')
        self.pixmap10 = QPixmap('IMG/jiating2.png')
        self.pixmap11 = QPixmap('IMG/xuanyi1.png')
        self.pixmap12 = QPixmap('IMG/xuanyi2.png')
        self.pixmap13 = QPixmap('IMG/ertong1.png')
        self.pixmap14 = QPixmap('IMG/ertong2.png')
        self.pixmap15 = QPixmap('IMG/xiju1.png')
        self.pixmap16 = QPixmap('IMG/xiju2.png')
        # 创建一个 QLabel 组件，并将照片设置为 QLabel 组件的图片
        self.label = QLabel()
        self.label.setPixmap(self.pixmap0)
        self.label1 = QLabel()
        self.label1.setPixmap(self.pixmap0)
        y.addWidget(self.label)
        y.addWidget(self.label1)
        # 创建下拉菜单
        self.combo_box = QComboBox()
        self.combo_box.addItem("爱情片")
        self.combo_box.addItem("喜剧片")
        self.combo_box.addItem("儿童片")
        self.combo_box.addItem("动作片")
        self.combo_box.addItem("家庭伦理片")
        self.combo_box.addItem("历史片")
        self.combo_box.addItem("内地片")
        self.combo_box.addItem("悬疑片")
        # 创建按钮
        self.button = QPushButton("加载数据")
        self.button.clicked.connect(self.load_data)
        self.button.clicked.connect(self.change_image)
        vlayout.addWidget(self.table)
        vlayout.addLayout(y)
        vlayout.addWidget(self.combo_box)
        vlayout.addWidget(self.button)
        self.setLayout(vlayout)

    def load_data(self):
        # 从下拉菜单中获取选择的数据表名
        table_name = self.combo_box.currentText()
        if table_name == '爱情片':
            table_name = 'aiqing'
        elif table_name == '内地片':
            table_name = 'neidi'
        elif table_name == '喜剧片':
            table_name = 'xiju'
        elif table_name == '儿童片':
            table_name = 'ertong'
        elif table_name == '动作片':
            table_name = 'dongzuo'
        elif table_name == '悬疑片':
            table_name = 'xuanyi'
        elif table_name == '历史片':
            table_name = 'lishi'
        elif table_name == '家庭伦理片':
            table_name = 'jiating'
        # 建立与数据库的连接
        # 须修改为自己数据库的账号密码
        cnx = pymysql.connect(user='root', password='123456', host='localhost', database='1905')
        cursor = cnx.cursor()
        # 查询数据库中的数据
        query = f'SELECT * FROM {table_name}'
        cursor.execute(query)
        rows = cursor.fetchall()
        # 删除表格中的所有行
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        # 获取数据表的字段名
        columns = [column[0] for column in cursor.description]
        # 设置表格的列数
        self.table.setColumnCount(len(columns))
        # 设置表格的行数
        self.table.setRowCount(len(rows))
        # 设置表格的表头
        self.table.setHorizontalHeaderLabels(columns)
        # 将数据加载到表格中
        for row_index, row in enumerate(rows):
            for column_index, data in enumerate(row):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row_index, column_index, item)

    def change_image(self):
        # 修改 QLabel 组件的图片
        # 从下拉菜单中获取选择的数据表名
        table_name = self.combo_box.currentText()
        if table_name == '爱情片':
            self.label.setPixmap(self.pixmap3)
            self.label1.setPixmap(self.pixmap4)
        elif table_name == '内地片':
            self.label.setPixmap(self.pixmap7)
            self.label1.setPixmap(self.pixmap8)
        elif table_name == '喜剧片':
            self.label.setPixmap(self.pixmap15)
            self.label1.setPixmap(self.pixmap16)
        elif table_name == '儿童片':
            self.label.setPixmap(self.pixmap13)
            self.label1.setPixmap(self.pixmap14)
        elif table_name == '动作片':
            self.label.setPixmap(self.pixmap1)
            self.label1.setPixmap(self.pixmap2)
        elif table_name == '悬疑片':
            self.label.setPixmap(self.pixmap11)
            self.label1.setPixmap(self.pixmap12)
        elif table_name == '历史片':
            self.label.setPixmap(self.pixmap5)
            self.label1.setPixmap(self.pixmap6)
        elif table_name == '家庭伦理片':
            self.label.setPixmap(self.pixmap9)
            self.label1.setPixmap(self.pixmap10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
