//Solucion 412 Fizz Buzz
#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> resultado;
        for (int i = 1; i <= n; i++) {
            if (i % 15 == 0)
                resultado.push_back("FizzBuzz");
            else if (i % 3 == 0)
                resultado.push_back("Fizz");
            else if (i % 5 == 0)
                resultado.push_back("Buzz");
            else 
                resultado.push_back(to_string(i));
        }
        return resultado;
    }
};

void print(vector<string> lista) {
    int n = lista.size();
    cout << "[";
    for (int i = 0; i < n - 1; i++) {
        cout << lista[i] << ", ";
    }
    cout << lista.back() << "]\n";
}

int main() {
    Solution solver;
    print(solver.fizzBuzz(3));
    print(solver.fizzBuzz(5));
    print(solver.fizzBuzz(15));

    return 0;
}