LETTERS = {
'A':(5, 2), # letter, common, max count allowed
'B':(2, 2),
'C': (2, 1),
'D': (2, 2),
'E': (10, 3),
'F': (2, 2),
'G': (2, 1),
'H': (4, 1),
'I': (5, 1),
'J': (1, 1),
'K': (1, 1),
'L': (4, 2),
'M': (2, 1),
'N': (5, 2),
'O': (6, 2),
'P': (2, 1),
'Qu': (1, 1),
'R': (5, 2),
'S': (7, 2),
'T': (10, 2),
'U': (2, 1),
'V': (2, 1),
'W': (3, 1),
'X': (1, 1),
'Y': (3, 2),
'Z': (1, 1) }

ROLL = ([5,5,5,5,6,6,6], 0, [2,2,2,2,3,3,3,3], [0,0,0,0,1,1,1,1,1,1])
# vowels , commen , uncommen, rare
DICE = (
('A', 'E', 'I', 'O', 'U'),
('H', 'L', 'N', 'R', 'S', 'T'),
('B', 'C', 'D', 'F', 'G', 'M', 'P', 'Y'),
('Z', 'X', 'Qu', 'K', 'J', 'V', 'W'))
            
# 00 04 08 12
# 01 05 09 13
# 02 06 10 14
# 03 07 11 15
ALLOWED_MOVEMENT = [
(1, 4, 5),
(0, 2, 4, 5, 6),
(1, 3, 5, 6, 7),
(2, 6, 7),
(0, 1, 5, 8, 9),
(0, 1, 2, 4, 6, 8, 9, 10),
(1, 2, 3, 5, 7, 9, 10, 11),
(2, 3, 6, 10, 11),
(4, 5, 9, 12, 13),
(4, 5, 6, 8, 10, 12, 13, 14),
(5, 6, 7, 9, 11, 13, 14, 15),
(6, 7, 10, 14, 15),
(8, 9, 13),
(8, 9, 10, 12, 14),
(9, 10, 11, 13, 15),
(10, 11, 14) ]