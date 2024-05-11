from PyQt6.QtWidgets import *
from gui7 import *



class Logic(QMainWindow, Ui_start_screen):
    def __init__(self) -> None:
        """
        this function sets up total and display strings as empty
        and links all buttons to their respective functions when clicked
        establishes that mode is not active when calculator is first opened
        :return: None
        """
        super().__init__()
        self.setupUi(self)
        self.total = ''
        self.status = False
        self.neg_count = 0
        self.count = 0
        self.display = ''
        self.modebutton.clicked.connect(lambda: self.mode())
        self.onebutton.clicked.connect(lambda: self.one())
        self.twobutton.clicked.connect(lambda: self.two())
        self.threebutton.clicked.connect(lambda: self.three())
        self.fourbutton.clicked.connect(lambda: self.four())
        self.fivebutton.clicked.connect(lambda: self.five())
        self.sixbutton.clicked.connect(lambda: self.six())
        self.sevenbutton.clicked.connect(lambda: self.seven())
        self.eightbutton.clicked.connect(lambda: self.eight())
        self.ninebutton.clicked.connect(lambda: self.nine())
        self.zerobutton.clicked.connect(lambda: self.zero())
        self.plusbutton.clicked.connect(lambda: self.add())
        self.minusbutton.clicked.connect(lambda: self.sub())
        self.multbutton.clicked.connect(lambda: self.mult())
        self.dividebutton.clicked.connect(lambda: self.div())
        self.enterbutton.clicked.connect(lambda: self.enter())
        self.clearbutton.clicked.connect(lambda: self.clear())
        self.modesubmit.clicked.connect(lambda: self.quad_submit())

    def clear(self) -> None:
        """
        clears all numeric data from calculator
        clears display
        :return: None
        """
        self.answer.setText("0")
        self.total = ""
        self.display = ''
        self.count = 0

    def one(self) -> None:
        """
        adds 1 to input in calculator as string
        displays additional 1 to input
        :return: None
        """
        self.total += '1'
        self.display += '1'
        self.answer.setText(self.display)

    def two(self) -> None:
        """
        adds 2 to input in calculator as string
        displays additional 2 to input
        :return: None
        """
        self.total += '2'
        self.display += '2'
        self.answer.setText(self.display)

    def three(self) -> None:
        """
        adds 3 to input in calculator as string
        displays additional 3 to input
        :return: None
        """
        self.total += '3'
        self.display += '3'
        self.answer.setText(self.display)

    def four(self) -> None:
        """
        adds number 4 to input and equation string
        and displays additional 4 to string
        :return: None
        """
        self.total += '4'
        self.display += '4'
        self.answer.setText(self.display)

    def five(self) -> None:
        """
        adds number 5 to input and equation string
        and displays additional 5 to string
        :return: None
        """
        self.total += '5'
        self.display += '5'
        self.answer.setText(self.display)

    def six(self) -> None:
        """
        adds number 6 to input and equation string
        and displays additional 6 to string
        :return: None
        """
        self.total += '6'
        self.display += '6'
        self.answer.setText(self.display)

    def seven(self) -> None:
        """
        adds number 7 to input and equation string
        and displays additional 7 to string
        :return: None
        """
        self.total += '7'
        self.display += '7'
        self.answer.setText(self.display)

    def eight(self) -> None:
        """
        adds number 8 to input and equation string
        and displays additional 8 to string
        :return: None
        """
        self.total += '8'
        self.display += '8'
        self.answer.setText(self.display)

    def nine(self) -> None:
        """
        adds number 9 to input and equation string
        and displays additional 9 to string
        :return: None
        """
        self.total += '9'
        self.display += '9'
        self.answer.setText(self.display)

    def zero(self) -> None:
        """
        adds number zero to input and equation string
        and displays additional zero to string
        :return: None
        """
        self.total += '0'
        self.display += '0'
        self.answer.setText(self.display)

    def add(self) -> None:
        """
        adds addition operator to equation
        clears display for next input
        :return: None
        """
        self.total += '+'
        self.display = ''

    def sub(self) -> None:
        """
        adds subtraction operator to equation
        clears display for next input
        :return: None
        """
        self.total += '-'
        self.display = ''

    def mult(self) -> None:
        """
        adds multiplication operator to equation
        clears display for next input
        :return: None
        """
        self.total += 'x'
        self.display = ''

    def div(self) -> None:
        """
        adds division operator to equation
        clears display for next input
        :return: None
        """
        self.total += '÷'
        self.display = ''

    def enter(self) -> None:
        """
        carries out equation stored to variable self.total
        looks for errors with zero division
        :return: None
        """
        try:
            if '+' in self.total:
                equation = self.total.split('+')
                ans = float(equation[0]) + float(equation[1])
                final_ans = str(ans)
                self.answer.setText(f'Ans= {final_ans}')
                self.total = ''
                self.display = ''

            elif '-' in self.total:
                equation = self.total.split('-')
                ans = float(equation[0]) - float(equation[1])
                final_ans = str(ans)
                self.answer.setText(f'Ans= {final_ans}')
                self.total = ''
                self.display = ''
            elif 'x' in self.total:
                equation = self.total.split('x')
                ans = float(equation[0]) * float(equation[1])
                final_ans = str(ans)
                self.answer.setText(f'Ans= {final_ans}')
                self.total = ''
                self.display = ''
            elif '÷' in self.total:
                equation = self.total.split('÷')
                ans = float(equation[0]) / float(equation[1])
                final_ans = str(ans)
                self.answer.setText(f'Ans= {final_ans}')
                self.total = ''
                self.display = ''
            else:
                equation = ''
        except ZeroDivisionError:
            self.answer.setText('Cannot divide by zero')
            self.total = ''
            self.display = ''
        except:
            self.answer.setText('Enter first number')
            self.total = ''
            self.display = ''

    def quad_submit(self) -> None:
        """
        calculates solutions of quadratic equation from input
        and displays them beneath input boxes
        :return: None
        """
        try:
            a = float(self.ainput.text())
            b = float(self.binput.text())
            c = float(self.cinput.text())
            first = (b ** 2) - (4*a*c)
            second = 2*a
            third = first ** (1/2)
            fourth = -1 * b
            try:
                answer1 = (fourth + third) / second
                fin1 = f'{answer1:.2f}'
                test1 = str(fin1)
            except:
                test1 = ('DNE')
            try:
                answer2 = (fourth - third) / second
                fin2 = f'{answer2:.2f}'
                test2 = str(fin2)
            except:
                test2 = ('DNE')
            if 'j' in test1:
                test1 = 'DNE'
            if 'j' in test2:
                test2 = 'DNE'
            self.errormessage.setText(f'Gimpel says:\nThe first solution is: {test1}\nThe second solution is: {test2}')
        except:
            self.errormessage.setText('Gimpel says:\nAll entries must be numeric.')
        self.ainput.setText("")
        self.binput.setText("")
        self.cinput.setText('')

    def mode(self) -> None:
        """
        disables buttons for each mode
        changes status whether mode is activated or deactivated
        :return: None
        """
        if self.status is False:
            self.status = True
        else:
            self.status = False
            self.errormessage.setText('')

        if self.status is True:

            self.answer.setEnabled(False)
            self.plusbutton.setEnabled(False)
            self.minusbutton.setEnabled(False)
            self.multbutton.setEnabled(False)
            self.dividebutton.setEnabled(False)
            self.onebutton.setEnabled(False)
            self.twobutton.setEnabled(False)
            self.threebutton.setEnabled(False)
            self.fourbutton.setEnabled(False)
            self.fivebutton.setEnabled(False)
            self.sixbutton.setEnabled(False)
            self.sevenbutton.setEnabled(False)
            self.eightbutton.setEnabled(False)
            self.ninebutton.setEnabled(False)
            self.zerobutton.setEnabled(False)
            self.ainput.setEnabled(True)
            self.binput.setEnabled(True)
            self.cinput.setEnabled(True)
            self.clearbutton.setEnabled(False)
            self.enterbutton.setEnabled(False)
            self.modesubmit.setEnabled(True)
        else:

            self.answer.setEnabled(True)
            self.plusbutton.setEnabled(True)
            self.minusbutton.setEnabled(True)
            self.multbutton.setEnabled(True)
            self.dividebutton.setEnabled(True)
            self.onebutton.setEnabled(True)
            self.twobutton.setEnabled(True)
            self.threebutton.setEnabled(True)
            self.fourbutton.setEnabled(True)
            self.fivebutton.setEnabled(True)
            self.sixbutton.setEnabled(True)
            self.sevenbutton.setEnabled(True)
            self.eightbutton.setEnabled(True)
            self.ninebutton.setEnabled(True)
            self.zerobutton.setEnabled(True)
            self.ainput.setEnabled(False)
            self.binput.setEnabled(False)
            self.cinput.setEnabled(False)
            self.modesubmit.setEnabled(False)
            self.clearbutton.setEnabled(True)
            self.enterbutton.setEnabled(True)
