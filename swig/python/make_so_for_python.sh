#!/bin/sh
#TODO:swigは個人で使えるようにしかなってない。どうやったら一般的にできるか？　とりあえず、cdで移動して、soは元のディレクトリにするようにしてる
#rm _numerical_expression_extractor.so
gcc -O2 -fPIC -c numerical_expression_extractor_wrap.cxx -I/home/katsuma/local/python/include/python2.7 -I/home/katsuma/usr/local/include -I../../src/
echo compiled nee_wrap.cxx
gcc -shared ../../build/src/numerical_expression_extractor.cpp.1.o ../../build/src/abstime_expression_normalizer.cpp.1.o ../../build/src/digit_utility.cpp.1.o ../../build/src/duration_expression_normalizer.cpp.1.o ../../build/src/normalizer_utility.cpp.1.o ../../build/src/number_normalizer.cpp.1.o ../../build/src/numerical_expression_normalizer.cpp.1.o ../../build/src/reltime_expression_normalizer.cpp.1.o numerical_expression_extractor_wrap.o -o _numerical_expression_extractor.so -I/home/katsuma/local/python/include/python2.7 -L/home/katsuma/usr/local/lib -lpficommon -lpficommon_visualization -lpficommon_text -lpficommon_network_base -lpficommon_concurrent -lpficommon_data -lpficommon_math -lpficommon_system -lpficommon_network_http -lpficommon_lang -lpficommon_network_rpc -lpficommon_network_cgi -lux
echo finished!
