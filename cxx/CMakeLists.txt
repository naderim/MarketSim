################################################################################
# MarketSim CMake
#
# @author: $Author$
#
# $Id:$
################################################################################

cmake_minimum_required (VERSION 3.4)

project (MarketSim)

#-------------------------------------------------------------------------------
# Build environment checks
#-------------------------------------------------------------------------------

message("CMAKE_SYSTEM=${CMAKE_SYSTEM} CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME} CMAKE_SYSTEM_VERSION=${CMAKE_SYSTEM_VERSION} CMAKE_SYSTEM_PROCESSOR=${CMAKE_SYSTEM_PROCESSOR}")

if (UNIX)
  message("Running in UNIX")
endif()

if (WIN32)
  message("Running in WIN32")
endif()

if (CYGWIN)
  message("Running in CYGWIN")
  message("compiler_version=$ENV{compiler_version}")
  if ("$ENV{compiler_version}" STREQUAL "clang")
    set(CMAKE_C_COMPILER   "clang")
    set(CMAKE_CXX_COMPILER "clang++")
  elseif ("$ENV{compiler_version}" STREQUAL "gcc")
    set(CMAKE_C_COMPILER   "gcc")
    set(CMAKE_CXX_COMPILER "g++")
  else()
    set(CMAKE_C_COMPILER   "x86_64-w64-mingw32-gcc")
    set(CMAKE_CXX_COMPILER "x86_64-w64-mingw32-g++")
  endif()
endif()

if (MINGW)
  message("Running in MINGW")
endif()

message("CMAKE_CXX_COMPILER_ID=${CMAKE_CXX_COMPILER_ID}")
if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
  message("using clang")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
  message("using gcc")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "Intel")
  message("using Intel C++")
elseif ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "MSVC")
  message("using Microsoft Visual Studio C++")
endif()

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU" OR "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
  message("Adding gcc flags")
  #using standard option -std=c++11 causes some errors on spdlog (fileno)
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -std=c++17" )
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -Wall -Werror")
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g -O3")
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -fpermissive")
endif()

if (NOT CYGWIN)
  set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -static-libstdc++ -static-libgcc" )
endif()

#-------------------------------------------------------------------------------
# Common
#-------------------------------------------------------------------------------

set(common_LIBS pthread boost_date_time)

if (NOT "$ENV{BOOST_HOME}" STREQUAL "")
  message("Using boost from $ENV{BOOST_HOME}")
  include_directories ("$ENV{BOOST_HOME}/include")
  link_directories ("$ENV{BOOST_HOME}/lib")
endif()

set (SPDLOG_VER 1.2.1)
#set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -DSPDLOG_TRACE_ON")
#set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -DSPDLOG_DEBUG_ON")
include_directories ("${PROJECT_SOURCE_DIR}/3rd-party/spdlog-${SPDLOG_VER}/include")

include_directories ("${PROJECT_SOURCE_DIR}/src")

file(GLOB_RECURSE common_SRC "src/*")
file(GLOB_RECURSE apps_SOURCES "src/apps/*")
list(REMOVE_ITEM common_SRC ${apps_SOURCES})

add_library(msim_lib ${common_SRC})

#-------------------------------------------------------------------------------
# msim
#-------------------------------------------------------------------------------

file(GLOB_RECURSE msim_SRC "src/apps/msim/*.cpp")
add_executable(msim ${msim_SRC})
target_link_libraries(msim msim_lib ${common_LIBS} boost_program_options)

#-------------------------------------------------------------------------------
# msimpy
#-------------------------------------------------------------------------------

#LIBRARIES += msimpy

#msimpy_SRCDIRS += $(COMMON_SUBDIRS)
#msimpy_SRCDIRS += apps/msimpy

#msimpy_CXXFLAGS += -I/usr/include/python2.7
##can not enable this as profile data is written on exit and this is a python module that does not exist
##msimpy_LDFLAGS += -pg
#msimpy_LDFLAGS += -g
#msimpy_LIBS += $(COMMON_LIBS)
#msimpy_LIBS += -lboost_python-py27 -lpython2.7

#file(GLOB_RECURSE msimpy_SRC "src/apps/msimpy/*.cpp")
#add_library (msimpy ${msimpy_SRC} ${common_SRC})
#target_include_directories(msimpy PUBLIC /usr/include/python2.7)
#target_link_libraries(msimpy ${common_LIBS} boost_python-py27 python2.7)


enable_testing ()
add_subdirectory (test)
