# TEST CMAKE-SWIG

Small test for generating a python interface to a C library using SWIG.

# Workflow

1. Build the cppcore library and test application using CMAKE
2. copy the generated _modfact.so / .lib and the modfact.py into the python directory
3. run simple python code :

        import modfact
        modfact.fact(3)

# OSX

- Install cmake, swig and Python3:
        
        brew install cmake
        brew install swig
        brew install python3
- in *test_swig_cmake/cppcore/bin* run the following commands:

        cmake ..
        cmake --build .

- in *test_swig_cmake/cppcore/bin/swig* run:

        python3
        import modfact
        modfact.fact(3)



## For Windows

- Install cmake and Visual studio 2019
- Extract SWIG from : http://www.swig.org/download.html (swigwin) binaries somewhere on the computer
- Add SWIG directory to the Path
- in *test_swig_cmake/cppcore/bin* run the following commands:

         cmake .. -A x64
         cmake --build . --config Release`


## Creating wheel

- in *test_swig_cmake/cppcore/bin* run the `make install` step
- in *test_swig_cmake/wheel* run the following commands

        python3 setup.py bdist_wheel

- a wheel should be built now.


