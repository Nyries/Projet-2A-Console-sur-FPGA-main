from instruction_recognition import*
from treatment import*
from virtual_register_fct import *
from virtual_memory_fct import virtual_memory_reset

def instruction_translation(ASM:str):
    """Programme global de traduction d'un code ASM en code machine
    code_ASM correspond au code brut tel qu'il est mis dans le terminal
    code-machine renvoie une liste instruction par instruction du code transcrit en code machine selon la convention LCM3
    """
    split_instructions=saut_ligne(ASM)
    #Les lignes des instructions sont numérotées à partir de 1
    line_instruction=[i+1 for i in range(len(split_instructions))]
    bitstream=[]
    register_update=[]
    line_pointer=0
    line_update=[0]
    memory_update=[]
    error=[]
    virtual_register_init()
    virtual_memory_reset()
    
    #Réalisation de la simulation
    split_instructions_with_END=split_instructions+["END"]
    j=0
    while split_instructions_with_END[line_pointer]!="END":
        instruction=split_instructions_with_END[line_pointer]
        register_update_instruction,line_pointer,memory_update_instruction,error_instruction=instruction_recognition(instruction,line_pointer,split_instructions,simu='ON')
        register_update.append(register_update_instruction)
        line_update.append(line_pointer)
        memory_update.append(memory_update_instruction)
        error=error+error_instruction
        j+=1
        if j>1000:
            error.append("There's an infinite loop at line "+str(line_pointer))
            error.append(line_pointer)
            break
        
#Réalisation du bitstream seulement si il n'y a pas d'erreurs
    if len(error)==0:
        i=0
        for instruction in split_instructions:
            bitstream.append(instruction_recognition(instruction,i,split_instructions,simu='OFF'))
            i+=1
    return split_instructions,line_instruction,bitstream,register_update,line_update,memory_update,error


