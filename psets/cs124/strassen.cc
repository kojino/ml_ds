#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>
#include <array>
#include <climits>
#include <cfloat>
#include <tuple>
#include <algorithm>
#include <fstream>
using namespace std;

void standard(int d, int A[d][d], int B[d][d], int C[d][d]) {
  for (int i = 0; i < d; i++) {
    for (int j = 0; j < d; j++) {
      for (int k = 0; k < d; k++) {
          C[i][k] += A[i][j] * B[j][k];
      }
    }
  }
}

int main(int argc, char *argv[]) {
  if (argc != 4)
  {
    cout << "Wrong number of input.";
  }
  else
  {
    int flag = atoi(argv[1]);
    int D = atoi(argv[2]);

    // open a file in read mode.
    ifstream infile;
    infile.open("afile.dat");

    int A[D][D];
    int B[D][D];
    int C[D][D];

    for (int i = 0; i < D; i++) {
      for  (int j = 0; j < D; j++) {
        infile >> A[i][j];
      }
    }
    for (int i = 0; i < D; i++) {
      for  (int j = 0; j < D; j++) {
        infile >> B[i][j];
      }
    }
    // close the opened file.
    infile.close();

    // Matrix Multiplication
    standard(D,A,B,C);

    for (int i = 0; i < D; i++) {
      for  (int j = 0; j < D; j++) {
        cout << C[i][j];
        cout << "\n";
      }
    }
  }
}