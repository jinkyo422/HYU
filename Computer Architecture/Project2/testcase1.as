        lw      0       1       five    load reg1 with 5 (symbolic address)
        lw      1       2       3       reg1에 대한 data hazard로 인해 하나의 noop과 forwarding 발생
start   add     1       2       1       reg2에 대한 data hazard로 인해 하나의 noop과 forwarding, reg1에 대한 forwarding 발생 
        beq     0       1       2       reg1에 대한 data hazard로 인해 forwarding 발생, reg1==0일 경우 branch hazard로 인해 세개의 noop 발생
        beq     0       0       start   start라벨로 항상 점프하므로 branch hazard로 인해 세개의 noop 발생
        noop
done    halt                            end of program
five    .fill   5
neg1    .fill   -1
stAddr  .fill   start                   will contain the address of start (2)
