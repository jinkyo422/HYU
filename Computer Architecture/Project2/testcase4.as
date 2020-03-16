        lw      0       1       five    load reg1 with 5 (symbolic address)
	noop
	noop
	noop
        lw      1       2       17      reg1에 대한 data hazard로 인해 lw이후에 3cycle이 필요하다
	noop
	noop
	noop
start   add     1       2       1       reg2에 대한 data hazard로 인해 lw이후에 3cycle이 필요하다
	noop
	noop
	noop
        beq     0       1       done    reg1에 대한 data hazard로 인해 add이후에 3cycle이 필요하다
	noop				branch hazard로 인해 beq이후에 3cycle이 필요하다
	noop
	noop
        beq     0       0       start   start라벨로 항상 점프하므로 branch hazard로 인해 세개의 noop 발생
	noop				branch hazard로 인해 beq이후에 3cycle이 필요하다
	noop
        noop
done    halt                            end of program
five    .fill   5
neg1    .fill   -1
stAddr  .fill   start                   will contain the address of start (2)
