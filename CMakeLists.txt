#=============================================================================
# Distributed under the Boost Software License, Version 1.0.
# See accompanying file LICENSE_1_0.txt or copy at
# http://www.boost.org/LICENSE_1_0.txt
#=============================================================================
cmake_minimum_required(VERSION 3.1 FATAL_ERROR)

set(CMAKE_DISABLE_SOURCE_CHANGES On)
set(CMAKE_DISABLE_IN_SOURCE_BUILD On)

set_property(GLOBAL PROPERTY USE_FOLDERS On)

project(Fenbu VERSION 0.1.1 LANGUAGES NONE)

find_package(PythonInterp REQUIRED)

find_program(PYTEST_EXECUTABLE NAME py.test)
find_program(PYLINT_EXECUTABLE NAME pylint)

if(NOT PYTEST_EXECUTABLE)
    message(WARNING "py.test not found.")
endif()
if(NOT PYLINT_EXECUTABLE)
    message(WARNING "pylint not found.")
endif()


enable_testing()


function(add_pylint _name)
    set(_target_dir "${CMAKE_CURRENT_BINARY_DIR}/${_name}.dir/")
    foreach(_src IN LISTS ARGN)
        get_filename_component(_abssrc ${_src} ABSOLUTE)
        string(MD5 _stamp "${_abssrc}")
        set(_stamp_file "${_target_dir}/${_stamp}.txt")
        list(APPEND _deps ${_stamp_file})
        add_custom_command(OUTPUT ${_stamp_file}
            DEPENDS ${_abssrc} "${PROJECT_SOURCE_DIR}/.pylintrc"
            COMMAND ${PYLINT_EXECUTABLE}  --rcfile "${PROJECT_SOURCE_DIR}/.pylintrc" ${_abssrc}
            COMMAND ${CMAKE_COMMAND} -E touch "${_stamp_file}"
        )
    endforeach()
    add_custom_target(${_name} ALL
        DEPENDS ${_deps}
        SOURCES ${ARGN}
    )
endfunction()

function(add_pytest _name)
    add_pylint(${_name} ${ARGN})
    set(_srcs)
    foreach(_src IN LISTS ARGN)
        get_filename_component(_abssrc ${_src} ABSOLUTE)
        list(APPEND _srcs ${_abssrc})
    endforeach()
    add_test(NAME ${_name} COMMAND ${PYTEST_EXECUTABLE} -v -r a ${_srcs})
endfunction()

add_pylint(pydht
    fenbu/bdecode.py
    fenbu/bencode.py
)

add_pytest(test_bencode test/test_bencode.py)
add_pytest(test_bdecode test/test_bencode.py)

