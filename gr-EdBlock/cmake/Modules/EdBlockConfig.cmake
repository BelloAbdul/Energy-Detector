INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_EDBLOCK EdBlock)

FIND_PATH(
    EDBLOCK_INCLUDE_DIRS
    NAMES EdBlock/api.h
    HINTS $ENV{EDBLOCK_DIR}/include
        ${PC_EDBLOCK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    EDBLOCK_LIBRARIES
    NAMES gnuradio-EdBlock
    HINTS $ENV{EDBLOCK_DIR}/lib
        ${PC_EDBLOCK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(EDBLOCK DEFAULT_MSG EDBLOCK_LIBRARIES EDBLOCK_INCLUDE_DIRS)
MARK_AS_ADVANCED(EDBLOCK_LIBRARIES EDBLOCK_INCLUDE_DIRS)

