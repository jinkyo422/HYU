# assignment1
- Employee Management

<input>
set 5
insert Shin 26 200 Personnel
insert Lee 24 180 Business
insert Kakao 36 300 Business
find Lee
insert Kim 38 280 Personnel
find Jeong
delete Kakao
inform Kakao
insert Park 21 270 Personnel
find Park
delete Jeong
insert Shin 31 390 Business
find Shin
inform Shin
insert Jeong 40 400 Personnel
avg Personnel
avg Purchase

<output>
1
-1
Not found
2
Not found
0
Shin 26 200 Personnel
Shin 31 390 Business
Not enough space
250
0

------------------------------
------------------------------

# assignment2
- Stack

<input>
( ( a b ) c d ) e f #
a b ( c ( d e ( f g ) ) h i ) #
( a ( b c d ) #
( a b c ( d e ) ) ) f g #
!

<output>
right. b a d c e f
right. a b g f e d i h c
wrong. d c b
wrong. e d c b a

------------------------------
------------------------------

# assignment3
- Linked List

<input>
i 7 0
i 2 7
i 1 0
i 4 8
i 5 7
s
d 7
i 6 2
d 3
i 3 5
f 7
f 3
f 1
s
e

<output>
Insert error. The 8 isn't in the list.
1 7 5 2
Delete error. The 3 isn't in the list.
Find error. The 7 isn't in the list.
The 3 is next of The 5
The 1 is next of The header.
1 5 3 2 6

------------------------------
------------------------------

# assignment4
- Absolute Value Min-Heap

<input>
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0

<output>
-1
1
0
-1
-1
1
1
-2
2
0

------------------------------
------------------------------

# assignment5
- Binary Search Tree

<input>
i 30
i 20
i 50
i 40
d 45
i 60
i 45
i 10
i 25
i 22
h 30
d 20
d 30
h 50
s
e

<output>
Not found
The height of the node (30) is 3
The height of the node (50) is 1
10 22 25 40 45 50 60

------------------------------
------------------------------

# assignment6
- DFS && BFS

<input>
4 5 1
1 2
1 3
1 4
2 4
3 4

<output>
1 2 4 3
1 2 3 4

------------------------------
------------------------------

# assignment7
- Dijkstra Algorithm

<input>
5
8
1 2 2
1 3 3
1 4 6
1 5 10
2 4 3
3 4 1
3 5 4
4 5 1
1 5

<output>
5

------------------------------
------------------------------

# assignment8
- Make a graded list

<input>
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhn 50 60 90
