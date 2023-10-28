#include<iostream>
#include<fstream>

int main()
{
    long long i;
    std::ifstream infile;
    infile.open("pointer.in");
    infile >> i;
    infile.close();
    char *p;
    p = (char *)malloc(1);
    p++;
    free(p);
    std::ofstream outfile;
    outfile.open("pointer.out");
    while(i--)
    outfile << *++p;
    outfile.close();
    return 0;
}