#Solucion #412 Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        resultado = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                resultado.append("FizzBuzz")
            elif i % 3 == 0: 
                resultado.append("Fizz")
            elif i % 5 == 0:
                resultado.append("Buzz")
            else: 
                resultado.append(str(i))
        return resultado            

solver = Solution()
print(solver.fizzBuzz(3))
print(solver.fizzBuzz(5))
print(solver.fizzBuzz(15))