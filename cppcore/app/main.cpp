//
// Created by Lucien on 14.12.20.
//

#include <iostream>
#include "modfact.h"

int main(int /*argc*/, char** /*argv*/) {
  std::cout << "C++ test program for SWIG and CMAKE" << std::endl;
  std::cout << "My_variable is: " << My_variable << std::endl;
  std::cout << "fact of 3 is:  " << fact(3) << std::endl;
  std::cout << "10 % 3 is: " << my_mod(10,3) << std::endl;
  return 0;
}
