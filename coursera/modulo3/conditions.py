print('B'>'A')
'''
Char.	ASCII	Char.	ASCII	Char.	ASCII	Char.	ASCII
A	    65	    N	    78	    a	    97	    n	    110
B	    66	    O	    79	    b	    98	    o	    111
C	    67	    P	    80	    c	    99	    p	    112
D	    68	    Q	    81	    d	    100	    q	    113
E	    69	    R	    82	    e	    101	    r	    114
F	    70	    S	    83	    f	    102	    s	    115
G	    71	    T	    84	    g	    103	    t	    116
H	    72	    U	    85	    h	    104	    u	    117
I	    73	    V	    86	    i	    105	    v	    118
J	    74	    W	    87	    j	    106	    w	    119
K	    75	    X	    88	    k	    107	    x	    120
L	    76	    Y	    89	    l	    108	    y	    121
M	    77	    Z	    90	    m	    109 	z	    122
#Equality operator
'''
age = 25
if age == 25:
    print("You are 25 years old.")
#Inequality operator
if age != 30:
    print("You are not 30 years old.")

#Greater than and less than

if age>= 20:
    print("Yes, the Age is greater than 20")

#The IF statement

age = 20
if age >= 21:
    print("You can enter the bar.")
else:
    print("Sorry, you cannot enter.")

#The ELIF Statement

if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry, you cannot do either.")
#Real-life example: Automated Teller Machine (ATM)
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = input("Enter the amount to withdraw: ")
    if amount % 10 == 0:
        dispense_cash(amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")

#The NOT operator
is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received")

#The AND operator

has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door()

# The Or Operator 
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    choose a movie()