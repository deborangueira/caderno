#include <iostream>
#include <cmath>

class Vetor2D {
    double x_, y_;
public:
    Vetor2D(double x=0, double y=0) : x_(x), y_(y) {}
    double norma() const { return std::sqrt(x_*x_ + y_*y_); }
    Vetor2D soma(const Vetor2D& o) const { return Vetor2D(x_ + o.x_, y_ + o.y_); }
    void print() const { std::cout << "(" << x_ << "," << y_ << ")"; }
};

int main() {
    Vetor2D a(3,4), b(1,2);
    Vetor2D c = a.soma(b);
    std::cout << "a="; a.print(); std::cout << " ||a||=" << a.norma() << "\n";
    std::cout << "b="; b.print(); std::cout << "\n";
    std::cout << "a+b="; c.print(); std::cout << "\n";
    return 0;
}
