class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        def isBulky(a, b, c, d):
            val = 10 ** 4

            if a >= val or b >= val or c >= val or d >= val:
                return True

            elif a * b * c >= (10 ** 9):
                return True

            return False

        def isHeavy(mass):
            if mass >= 100:
                return True

            return False
        
        x = isBulky(length, width, height, mass)
        y = isHeavy(mass)

        if x and y:
            return "Both"
        elif y and not x:
            return "Heavy"
        elif x and not y:
            return "Bulky"
        else:
            return "Neither"
