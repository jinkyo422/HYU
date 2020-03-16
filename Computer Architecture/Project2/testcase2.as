        lw      0       1       input   load reg1 with 20 (symbolic address)
        add     1       1       2       reg1에 대한 data hazard로 인해 하나의 noop과 forwarding 발생
        add     2       2       3       reg2를 forwarding하여 data hazard 처리
        add     3       3       3       reg3를 forwarding하여 data hazard 처리
        add     2       3       1       reg2와 reg3을 forwarding하여 data hazard 처리
        noop
        halt
input   .fill   20
pos1    .fill   1
mempos  .fill   100
