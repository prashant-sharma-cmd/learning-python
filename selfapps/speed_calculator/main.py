import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QLabel, \
    QLineEdit, QWidget, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Defining Widgets
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        self.unit = QComboBox()
        self.unit.addItems(["Metric (km)", "Imperial (miles)"] )

        time_label = QLabel("Time")
        self.time_line_edit = QLineEdit()

        button = QPushButton("Calculate")
        button.clicked.connect(self.calculate)
        self.output = QLabel("")

        # Displaying Widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(button, 2, 1)
        grid.addWidget(self.output, 3, 1)

        self.setLayout(grid)

    def calculate(self) -> None:
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance / time
        index = self.unit.currentIndex()
        if index == 0:
            speed = round(speed, 2)
            unit = "km/hr"
        else:
            speed = round(speed * 0.621371, 2)
            unit = "mph"
        self.output.setText(f"Average Speed: {speed} {unit}")



app = QApplication(sys.argv)
window = SpeedCalculator()
window.show()
app.exit(app.exec())