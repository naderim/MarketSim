################################################################################
# MarketSim Tests CMake
#
# @author: $Author$
#
# $Id:$
################################################################################



set(utest_LIBS msim_lib msim_testutils ${common_LIBS} boost_unit_test_framework)
set(boost_utest_cmd_opts --report_level=detailed --log_level=all)
include_directories ("${PROJECT_SOURCE_DIR}/test")

file(GLOB_RECURSE utest_SRC "*.cpp")
file(GLOB_RECURSE utest_ut_LIST "*.ut.cpp")
file(GLOB_RECURSE utest_t_LIST "*.t.cpp")

list(REMOVE_ITEM utest_SRC ${utest_ut_LIST})
list(REMOVE_ITEM utest_SRC ${utest_t_LIST})
add_library(msim_testutils ${utest_SRC})


add_executable(utest ${utest_t_LIST})
target_compile_definitions(utest PUBLIC BOOST_TEST_DYN_LINK)
target_link_libraries(utest ${utest_LIBS})
add_test (NAME utest COMMAND ./utest ${boost_utest_cmd_opts})

foreach (utest_ut_PATH ${utest_ut_LIST})
  get_filename_component(utest_ut_TARGET0 ${utest_ut_PATH} NAME)
  string(REGEX REPLACE "\\.[^.]*$" "" utest_ut_TARGET ${utest_ut_TARGET0})
  string(REGEX REPLACE "\\..*$" "UnitTest" utest_ut_MODULE ${utest_ut_TARGET0})
  message("+ Adding Unit Test ${utest_ut_TARGET}")
  add_executable(${utest_ut_TARGET} ${utest_ut_PATH})
  target_compile_definitions(${utest_ut_TARGET} PUBLIC BOOST_TEST_MODULE=${utest_ut_MODULE} )
  target_compile_definitions(${utest_ut_TARGET} PUBLIC BOOST_TEST_DYN_LINK )
  target_link_libraries(${utest_ut_TARGET} ${utest_LIBS})
  add_test (NAME ${utest_ut_TARGET} COMMAND ./${utest_ut_TARGET} ${boost_utest_cmd_opts})
endforeach(utest_ut_PATH)
