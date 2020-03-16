        lw      0       2       mcand
        lw      0       3       mplier
        lw      0       4       index
start	nor	3	3	3
	nor	4	4	4
	nor	3	4	5
	nor	3	3	3
	nor	4	4	4
	beq	0	5	L1
	add	2	1	1
	add	4	6	6
L1	beq	3	6	done
	add	4	4	4
	add	2	2	2
	beq	0	0	start
done    halt
mcand   .fill   32766
mplier  .fill   10383
index   .fill   1
