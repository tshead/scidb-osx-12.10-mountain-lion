# to find boost libraries which harness requires 
#message("${Boost_LIBRARIES}  before setting........................................................................")
#we dont have to add system, options, serialization as they are already added
#find_package(Boost REQUIRED system program_options serialization filesystem thread regex) 
#find_package(Boost REQUIRED filesystem thread regex)
#message("${Boost_LIBRARIES}  after setting........................................................................")

include_directories("include")

#_____________________________________________________________________________________________________________
# scidbtest #
#___________#
set(scidbtest_src
	src/helper.cpp
	src/errdb.cpp
	src/Exceptions.cpp
	src/defaultexecutor.cpp
	src/harnesstestexecutor.cpp
	src/executorfactory.cpp
	src/scidbtestcaseexecutor.cpp
	src/scidbtest.cpp	
)
add_executable(scidbtest ${scidbtest_src})
set_target_properties(scidbtest PROPERTIES COMPILE_FLAGS "--pedantic -Wall -Wno-long-long -g -DSCIDB_CLIENT")
target_link_libraries(scidbtest ${Boost_LIBRARIES} ${LOG4CXX_LIBRARIES} scidbclient ${LIBRT_LIBRARIES} )
if(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
	set_target_properties(scidbtest PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=2")
else(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
	set_target_properties(scidbtest PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=3")
endif(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)

#_____________________________________________________________________________________________________________
# scidbtestharness #
#__________________#
set(common_sources
	src/helper.cpp
	src/errdb.cpp
	src/Exceptions.cpp
	src/executorfactory.cpp
	src/defaultexecutor.cpp
    src/harnesstestexecutor.cpp
	src/xmlarchive.cpp
	src/reporter.cpp
	src/manager.cpp
	src/suite.cpp
	src/harness.cpp
)

set(scidbtestharness_src
    ${common_sources}
	src/main.cpp
)

add_executable(scidbtestharness ${scidbtestharness_src})
extractDebugInfo("${GENERAL_OUTPUT_DIRECTORY}" "scidbtestharness" scidbtestharness)
target_link_libraries(scidbtestharness scidbclient ${LIBRT_LIBRARIES} )
 
if(NOT (${DISTRO_NAME_VER} MATCHES "RedHat-[0-9][.][0-9]"))
    target_link_libraries(scidbtestharness ${Boost_LIBRARIES} ${LOG4CXX_LIBRARIES})
endif()

set_target_properties(scidbtestharness
	PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${GENERAL_OUTPUT_DIRECTORY}
    BUILD_WITH_INSTALL_RPATH TRUE
	CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE
	INSTALL_RPATH ${DEFAULT_RPATH}	
	COMPILE_FLAGS "-DSCIDB_CLIENT"
)
    
if(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
        set_target_properties(scidbtestharness PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=2")
else(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
        set_target_properties(scidbtestharness PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=3")
endif(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)

configure_file(test_config.ini config.ini)
configure_file(runN.py "${GENERAL_HARNESSTEST_DIRECTORY}/runN.py" COPYONLY)
configure_file(scidbtestprep.py "${GENERAL_OUTPUT_DIRECTORY}/scidbtestprep.py" COPYONLY)
configure_file(mu_admin.py "${GENERAL_OUTPUT_DIRECTORY}/mu_admin.py")
configure_file(log4j.properties "${GENERAL_OUTPUT_DIRECTORY}/log4j.properties" COPYONLY)
configure_file("testcases/t/client/basic.py.in" "${GENERAL_HARNESSTEST_DIRECTORY}/testcases/t/client/basic.py")
configure_file("testcases/t/client/querylist.csv"  "${GENERAL_HARNESSTEST_DIRECTORY}/testcases/t/client/querylist.csv")

#_____________________________________________________________________________________________________________
# CDASH report #
#______________#

set(preparecdashreport_sources
	src/helper.cpp
	src/errdb.cpp
	src/Exceptions.cpp
	src/xmlarchive.cpp
	src/reporter.cpp
	src/cdashreportstructs.cpp
	src/cdashreportapp.cpp
	src/preparecdashreport.cpp
)

add_executable(preparecdashreport ${preparecdashreport_sources})
set_target_properties(preparecdashreport PROPERTIES COMPILE_FLAGS "--pedantic -Wall -Wno-long-long -g -DSCIDB_CLIENT")
target_link_libraries(preparecdashreport ${Boost_LIBRARIES} ${LOG4CXX_LIBRARIES} ${LIBRT_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT} )
if(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
        set_target_properties(preparecdashreport PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=2")
else(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)
        set_target_properties(preparecdashreport PROPERTIES COMPILE_DEFINITIONS "BOOST_FS_VER=3")
endif(${Boost_MAJOR_VERSION} LESS 2 AND ${Boost_MINOR_VERSION} LESS 46)

#_____________________________________________________________________________________________________________
# misc #
#______#

set(arg_separator_sources
	src/arg_separator.cc
)

add_executable(arg_separator ${arg_separator_sources})
extractDebugInfo("${GENERAL_OUTPUT_DIRECTORY}" "arg_separator" arg_separator)
set_target_properties(arg_separator PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${GENERAL_OUTPUT_DIRECTORY})
