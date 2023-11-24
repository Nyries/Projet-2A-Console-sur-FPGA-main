from instruction_translation import *
from virtual_register_fct import*


ASM='MOV R0,#2\nLSL R1,R0,#28\nSTR R0,[R1]\nLDR R2,[R1]'
print(instruction_translation(ASM))
print(virtual_register)