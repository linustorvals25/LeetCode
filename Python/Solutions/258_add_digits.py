# 258 Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num > 0:
            num, resto = divmod(num, 10)
            total += resto
        if total > 9:
            return self.addDigits(total)
        return total
    
if __name__ == '__main__':
    solver = Solution()
    x = 0
    print(f'La suma de los digitos de {x = } es: {solver.addDigits(x)}')
    x = 38
    print(f'La suma de los digitos de {x = } es: {solver.addDigits(x)}')
    x = 123
    print(f'La suma de los digitos de {x = } es: {solver.addDigits(x)}')
    