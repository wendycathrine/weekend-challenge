#!/usr/bin/env python

import MyModule

MyModule.addNumbers(2,2)

MyModule.subtractNumbers(20,45)

MyModule.power(2,7)

from MyModuleimport employee1 #import a specific function/part
print(employee1["firstname"])

for k,v in employee1.items():
    print(f"{k}:{v}")

#in-built module
# platform module
test1 = platform.system()
print(test1)
