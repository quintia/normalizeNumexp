AR = '/usr/bin/ar'
ARFLAGS = 'rcs'
BINDIR = '/usr/local/bin'
CC_VERSION = ('4', '6', '1')
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-O2', '-Wall', '-g', '-pipe']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEFINES = ['HAVE_PFICOMMON=1', 'HAVE_UX=1']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
HAVE_PFICOMMON = 1
HAVE_UX = 1
INCLUDES_PFICOMMON = ['/home/katsuma/usr/local/include']
INCLUDES_UX = ['/home/katsuma/usr/local/include']
LIBDIR = '/usr/local/lib'
LIBPATH_PFICOMMON = ['/home/katsuma/usr/local/lib']
LIBPATH_ST = '-L%s'
LIBPATH_UX = ['/home/katsuma/usr/local/lib']
LIB_GTEST_PTHREAD = ['pthread']
LIB_PFICOMMON = ['pficommon', 'pficommon_visualization', 'pficommon_text', 'pficommon_network_base', 'pficommon_concurrent', 'pficommon_data', 'pficommon_math', 'pficommon_system', 'pficommon_network_http', 'pficommon_lang', 'pficommon_network_rpc', 'pficommon_network_cgi']
LIB_ST = '-l%s'
LIB_UX = ['ux']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CXX = ['/usr/bin/g++']
PKGCONFIG = '/usr/bin/pkg-config'
PREFIX = '/usr/local'
RPATH_ST = '-Wl,-rpath,%s'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
UNITTEST_GTEST_PATH = '/home/katsuma/src/normalizeNumexp/normalizeNumexp/.unittest-gtest'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_PFICOMMON', 'HAVE_UX']
macbundle_PATTERN = '%s.bundle'
