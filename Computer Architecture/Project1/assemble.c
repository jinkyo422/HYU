/* Assembler code fragment for LC-2K */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAXLINELENGTH 1000

int readAndParse(FILE *, char *, char *, char *, char *, char *);
int isNumber(char *);
int branch(FILE *, char *);

int
main(int argc, char *argv[])
{
    char *inFileString, *outFileString;
    FILE *inFilePtr, *outFilePtr, *inFilePtr2;
    char label[MAXLINELENGTH], opcode[MAXLINELENGTH], arg0[MAXLINELENGTH], arg1[MAXLINELENGTH], arg2[MAXLINELENGTH];
    
    if (argc != 3) {
        printf("error: usage: %s <assembly-code-file> <machine-code-file>\n", argv[0]);
        exit(1);
    }
    
    inFileString = argv[1];
    outFileString = argv[2];
    
    inFilePtr = fopen(inFileString, "r");
    inFilePtr2 = fopen(inFileString, "r");
    if (inFilePtr == NULL || inFilePtr2 == NULL) {
        printf("error in opening %s\n", inFileString);
        exit(1);
    }
    outFilePtr = fopen(outFileString, "w");
    if (outFilePtr == NULL) {
        printf("error in opening %s\n", outFileString);
        exit(1);
    }
    
    while(readAndParse(inFilePtr, label, opcode, arg0, arg1, arg2)) {
        if (strcmp(label, "")) {
            int flag = 0;
            char temp[MAXLINELENGTH];
            while (readAndParse(inFilePtr2, temp, opcode, arg0, arg1, arg2)) {
                if (!strcmp(label, temp))
                    flag++;
            }
            if (flag > 1) {
                printf("error: duplicate label\n");
                exit(1);
            }
            rewind(inFilePtr2);
        }
    }
    rewind(inFilePtr);
    rewind(inFilePtr2);
    
    int pc = 0;
    while(readAndParse(inFilePtr, label, opcode, arg0, arg1, arg2)) {
        int op;
        int num0, num1, offset;
        int result;
        
        if (!strcmp(opcode, "add")) {
            op = 0;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            offset = atoi(arg2);
        }
        else if (!strcmp(opcode, "nor")) {
            op = 1;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            offset = atoi(arg2);
        }
        else if (!strcmp(opcode, "lw")) {
            op = 2;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            if (isNumber(arg2))
                offset = atoi(arg2);
            else
                offset = branch(inFilePtr2, arg2);
        }
        else if (!strcmp(opcode, "sw")) {
            op = 3;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            if (isNumber(arg2))
                offset = atoi(arg2);
            else
                offset = branch(inFilePtr2, arg2);
        }
        else if (!strcmp(opcode, "beq")) {
            op = 4;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            if (isNumber(arg2))
                offset = atoi(arg2);
            else
                offset = branch(inFilePtr2, arg2) - pc - 1;
        }
        else if (!strcmp(opcode, "jalr")) {
            op = 5;
            num0 = atoi(arg0);
            num1 = atoi(arg1);
            offset = 0;
        }
        else if (!strcmp(opcode, "halt")) {
            op = 6;
            num0 = 0;
            num1 = 0;
            offset = 0;
        }
        else if (!strcmp(opcode, "noop")) {
            op = 7;
            num0 = 0;
            num1 = 0;
            offset = 0;
        }
        else if (!strcmp(opcode, ".fill")) {
            if (isNumber(arg0)) {
                result = atoi(arg0);
                fprintf(outFilePtr, "%d\n", result);
                pc++;
                continue;
            }
            else {
                result = branch(inFilePtr2, arg0);
                fprintf(outFilePtr, "%d\n", result);
                pc++;
                continue;
            }
        }
        else {
            printf("error: unrecognized opcode\n%s\n", opcode);
            exit(1);
        }
        if (offset < -32768 || offset > 32767) {
            printf("error: offsetField overflow\n");
            exit(1);
        }
        if (offset < 0)
            offset += 65536;
        
        result = op * 4194304 + num0 * 524288 + num1 * 65536 + offset;
        
        fprintf(outFilePtr, "%d\n", result);
        pc++;
    }
    
    return(0);
}

/*
 * Read and parse a line of the assembly-language file. Fields are returned
 * in label, opcode, arg0, arg1, arg2 (these strings must have memory already
 * allocated to them).
 *
 * Return values:
 *   0 if reached end of file
 *   1 if all went well
 *
 * exit(1) if line is too long.
 */
int
readAndParse(FILE *inFilePtr, char *label, char *opcode, char *arg0, char *arg1, char *arg2)
{
    char line[MAXLINELENGTH];
    char *ptr = line;
     
    /* delete prior values */
    label[0] = opcode[0] = arg0[0] = arg1[0] = arg2[0] = '\0';
     
    /* read the line from the assembly-language file */
    if (fgets(line, MAXLINELENGTH, inFilePtr) == NULL) {
         /* reached end of file */
         return(0);
    }
     
    /* check for line too long (by looking for a \n) */
    if (strchr(line, '\n') == NULL) {
         /* line too long */
         printf("error: line too long\n");
         exit(1);
    }
     
    /* is there a label? */
    ptr = line;
    if (sscanf(ptr, "%[^\t\n\r ]", label)) {
         /* successfully read label; advance pointer over the label */
         ptr += strlen(label);
    }
     
    /*
     * Parse the rest of the line. Would be nice to have real regular
     * expressions, but scanf will suffice.
     */
    sscanf(ptr, "%*[\t\n\r ]%[^\t\n\r ]%*[\t\n\r ]%[^\t\n\r ]%*[\t\n\r ]%[^\t\n\r ]%*[\t\n\r ]%[^\t\n\r ]", opcode, arg0, arg1, arg2);
    return(1);
}

int
isNumber(char *string)
{
    /* return 1 if string is a number */
    int i;
    return( (sscanf(string, "%d", &i)) == 1);
}

int
branch(FILE *inFilePtr2, char *destination)
{
    int address;
    int count = 0;
    int flag = 0;
    char label[MAXLINELENGTH], opcode[MAXLINELENGTH], arg0[MAXLINELENGTH], arg1[MAXLINELENGTH], arg2[MAXLINELENGTH];

    rewind(inFilePtr2);
    while (readAndParse(inFilePtr2, label, opcode, arg0, arg1, arg2)) {
        if (!strcmp(label, destination)) {
            address = count;
            flag = 1;
        }
        count++;
    }
    if (flag == 0) {
        printf("error: label does not exist\n");
        exit(1);
    }
    return address;
}
