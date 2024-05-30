"""
Класс будильник-выключатель
"""


class DimmerSwitch:

    def __init__(self):
        self.brightness = 0
        self.switch_is_On = False

    def turn_On(self):
        self.switch_is_On = True

    def turn_Off(self):
        self.switch_is_On = False

    def raise_brightness(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_brightness(self):
        if self.brightness > 0:
            self.brightness -= 1

    # Дополнительный метод для отладки
    def show(self):
        print('Switch is on?', self.switch_is_On)
        print('Brightness is:', self.brightness)



switcher = DimmerSwitch()
switcher.raise_brightness()
switcher.raise_brightness()
switcher.raise_brightness()
print(switcher.brightness)
switcher.lower_brightness()
switcher.lower_brightness()
print(switcher.brightness)
switcher.lower_brightness()
switcher.lower_brightness()
print(switcher.brightness)
switcher.lower_brightness()
print(switcher.brightness)
switcher.show()