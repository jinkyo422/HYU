        lw      0       1       input   load reg1 with 10 (symbolic address)
        noop
	noop
	noop
	add	0	1	2	reg1에 대한 data hazard로 인해 lw이후에 3cycle이 필요하다
	noop
	noop
	noop
	beq	1	2	4	reg2에 대한 data hazard로 인해 add이후에 3cycle이 필요하다
	noop				branch hazard로 인해 beq이후에 3cycle이 필요하다
	noop
	noop
	add	1	2	3
	halt
input   .fill   10
