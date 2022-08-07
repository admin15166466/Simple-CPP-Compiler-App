import os
lujing=input("Enter C++ Code File/输入C++需要编译的.cpp文件路径:")
os.system("g++ "+lujing)
os.system("./a.out")
print("")
os.system("rm -rf a.out")
