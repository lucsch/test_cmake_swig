# This is a CMake example for Python

FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

FIND_PACKAGE(PythonLibs 3 REQUIRED)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})

SET(CMAKE_SWIG_FLAGS "")

SET_SOURCE_FILES_PROPERTIES(modfact.i PROPERTIES CPLUSPLUS ON)
SET_SOURCE_FILES_PROPERTIES(modfact.i PROPERTIES SWIG_FLAGS "-includeall")
SWIG_ADD_MODULE(modfact python modfact.i "../modfact/src/modfact.cpp" "../modfact/src/modfact.h")
SWIG_LINK_LIBRARIES(modfact ${PYTHON_LIBRARIES})
MESSAGE("Python libs: ${PYTHON_LIBRARIES}")

# install
install(TARGETS modfact DESTINATION "${PROJECT_SOURCE_DIR}/wheel/modfact" )
install(FILES  "${CMAKE_BINARY_DIR}/swig/modfact.py" DESTINATION "${PROJECT_SOURCE_DIR}/wheel/modfact")
if(MSVC)
    install(FILES  "${CMAKE_BINARY_DIR}/swig/_modfact.pyd" DESTINATION "${PROJECT_SOURCE_DIR}/wheel/modfact")
else(MSVC)
    install(FILES "${CMAKE_BINARY_DIR}/swig/_modfact.so" DESTINATION "${PROJECT_SOURCE_DIR}/wheel/modfact")
endif(MSVC)
