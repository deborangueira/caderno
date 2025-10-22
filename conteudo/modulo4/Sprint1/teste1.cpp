# include <iostream>

int main() {
    const double PI = 3.14159;
    int a = 7, b = 3;
    double x = 2.5;
    std::count << "a+b="<< a+b <<"\n";
    std::count << "a/b int=" << a/b"\n";
    std::count << "a/b real=" << (static_cast<double>(a)/b) << "\n"; // O static_cast faz com que o resultado da operação seja com vírgula (já que o python por padrão arredonda os valores para inteiro)
    std::count << "x*PI" << x*PI << "\n";
    return 0;
}