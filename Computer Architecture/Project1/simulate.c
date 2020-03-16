/* LC-2K Instruction-level simulator */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NUMMEMORY 65536 /* maximum number of words in memory */
#define NUMREGS 8 /* number of machine registers */
#define MAXLINELENGTH 1000

typedef struct stateStruct {
    int pc;
    int mem[NUMMEMORY];
    int reg[NUMREGS];
    int numMemory;
} stateType;

void printState(stateType *);
int convertNum(int);

int
main(int argc, char *argv[])
{
    char line[MAXLINELENGTH];
    stateType state;
    FILE *filePtr;
    
    if (argc != 2) {
        printf("error: usage: %s <machine-code file>\n", argv[0]);
        exit(1);
    }
    
    filePtr = fopen(argv[1], "r");
    if (filePtr == NULL) {
        printf("error: can't open file %s", argv[1]);
        perror("fopen");
        exit(1);
    }
    
    state.pc = 0;
    for (int i = 0; i < NUMREGS; i++)
        state.reg[i] = 0;
    
    /* read in the entire machine-code file into memory */
    for (state.numMemory = 0; fgets(line, MAXLINELENGTH, filePtr) != NULL; state.numMemory++) {
        
        if (sscanf(line, "%d", state.mem+state.numMemory) != 1) {
            printf("error in reading address %d\n", state.numMemory);
            exit(1);
        }
        printf("memory[%d]=%d\n", state.numMemory, state.mem[state.numMemory]);
    }
    printf("\n");
    
    int opcode;
    int regA;
    int regB;
    int offset;
    int count = 0;
    while(1){
        count++;
        printState(&state);
        opcode = (state.mem[state.pc] >> 22) & 7;
        regA = (state.mem[state.pc] >> 19) & 7;
        regB = (state.mem[state.pc] >> 16) & 7;
        offset = convertNum(state.mem[state.pc] & 65535);
        
        switch (opcode) {
            case 0:
                state.reg[offset] = state.reg[regA] + state.reg[regB];
                break;
                
            case 1:
                state.reg[offset] = ~(state.reg[regA] | state.reg[regB]);
                break;
                
            case 2:
                state.reg[regB] = state.mem[state.reg[regA] + offset];
                break;
                
            case 3:
                state.mem[state.reg[regA] + offset] = state.reg[regB];
                break;
                
            case 4:
                if (state.reg[regA] == state.reg[regB])
                    state.pc += offset;
                break;
                
            case 5:
                state.reg[regB] = state.pc + 1;
                state.pc = state.reg[regA] - 1;
                break;

            case 6:
                printf("machine halted\ntotal of %d instructions executed\nfinal state of machine:\n", count);
                state.pc++;
                printState(&state);
                break;
                
            case 7:
                break;
        }
        
        if(opcode == 6)
            break;
        
        state.pc++;
    }
    
    return(0);
}

void
printState(stateType *statePtr)
{
    int i;
    printf("\n@@@\nstate:\n");
    printf("\tpc %d\n", statePtr->pc);
    printf("\tmemory:\n");
    for (i=0; i<statePtr->numMemory; i++) {
        printf("\t\tmem[ %d ] %d\n", i, statePtr->mem[i]);
    }
    printf("\tregisters:\n");
    for (i=0; i<NUMREGS; i++) {
        printf("\t\treg[ %d ] %d\n", i, statePtr->reg[i]);
    }
    printf("end state\n");
}

int
convertNum(int num) {
    /* convert a 16-bit number into a 32-bit Linux integer */
    if (num & (1 << 15)) {
        num -= (1 << 16);
    }
    return (num);
}
