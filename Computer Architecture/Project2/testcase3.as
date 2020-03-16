	lw      0       1       one     load reg1 with 1
        lw      0       2       two     load reg2 with 2
        noop
	noop
        add     0       1       3       reg1에 대한 data hazard로 인해 lw이후에 3cycle이 필요하다
        add     0       2       1       reg2에 대한 data hazard로 인해 lw이후에 3cycle이 필요하다
	noop
	noop
        add     0       3       2       reg3에 대한 data hazard로 인해 add이후에 3cycle이 필요하다
        noop
done    halt                            end of program
one    .fill   1
two    .fill   2
