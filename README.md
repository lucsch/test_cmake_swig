TEST CMAKE-SWIG

Small test for generating a python interface to a C library using SWIG.

1. Build the cppcore library using CMAKE
2. copy the generated _modfact.so / dll and the modfact.py into the python directory
3. run simple python code :

    import modfact
    modfact.fact(3)