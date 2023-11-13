1. Create a prod3 () function that takes three integers as parameters and returns the product of the three. For example:

>>> prod3(4, 2, 10)
80
>>> prod3(1, 2, -3)
-9
>>> prod3(0, 10300, 24)
0


2. Create a quadProd3 () function that has three integers as parameters and returns the product of the squares of the three numbers. This function must use both prod3() and square() (from the slides).

>>> quadProd3(1, 2, 3)
36
>>> quadProd3(-2, 4, 9)
5184
>>> quadrProd(-1, -1, 2)
2


3. A person's BMI is calculated according to the formula:

BMI = weight / height**2

Build a function called bmi(weight, height) that takes a person's weight and height as parameters and returns the person's BMI. Create tests for this function.

>>> bmi(80, 1.8)
24.691358
>>> bmi(50, 1.7)
17.301038
>>> bmi(100, 1.85)
29.21840


4. There are several formulas for predicting a person's body fat percentage based on their BMI. One of them is the following:

 CG = 1.294 * BMI + 0.2 * age - 11.4 * gender - 0.8

Build a bodyFat() function that, given a person's height, weight, age, and gender (0 for men, 1 for women), returns an estimate of their body fat percentage. This function must use the bmi() function that you implemented before.

>>> cg(24.69135880, 43, 0)
45.608619430241056
>>> cg(17.301038, 20, 1)
29.608619430241053
>>> cg(29.21840, 50, 1)
35.608619430241056


5. Build a dividend() function that has three parameters, the rest, the quotient, and divisor of a division, and returns the corresponding dividend. For example:

dividend(1, 3, 3)   # returns 10
dividend(42, 9, 43) # returns 429
dividend(6, 13, 7) # returns 97


6. Build a program that reads two strings from the keyboard and determines whether the two have the same length. The program should take the results of reading the inputs via keyboard and pass them to a function called compareLengths() that compares the lengths of the strings and returns True if they are the same length and False if they are not. The length of a string can be obtained using the predefined len() function:

>>> len ("abcde")
5 

The following presents a few examples of usage of compareLengths():

>>> compareLengths("PSV Eindhoven", "FC Utrecht")
False
>>> compareLenghts("SNSD", "2NE1")
True
>>> compareLenghts("Zebras and Giraffes are just fake Okapis", "Red pandas are not pandas but still cute")
True


7. Make a sumDigits() function that takes a number of up to three digits as a parameter and returns the sum of those digits:

>>> sumDigits (123)
6
>>> sumDigits (335)
11
>>> sumDigits (11)
2

Tip: the integer division (//) and rest of the division (%) operators are very useful in this exercise.


8. Make a sumManyDigits() function that takes a number of up to nine digits as a parameter and returns the sum of those digits. It is suggested that this function uses the sumDigits() function from the previous exercise. Examples:

>>> sumManyDigits (66)
12
>>> sumManyDigits (1335)
12
>>> sumManyDigits (98765432)
44


9. Create a function that takes three integers as parameters and prints all three in ascending order

>>> orderInts(3,4,-3) # they can be printed in the same lines or different lines
-3 
3
4
>>> orderInts(100, 100, 200)
100
100
200
>>> orderInts(-9, -10, -3)
-10
-9
-3

10. Build a function that takes a string containing only one character as a parameter and tells you whether it is alphabetic (returns 0), numeric (returns 1), or neither (returns -1). If the string has more than one character, your program should print an error message. The length of a string can be obtained as follows:

>>> len ("abc") 
3

Examples:

>>> alpha('b')
0
>>> alpha('9')
1
>>> alpha('}')
-1
>>> alpha("abc")
Error! The parameter should consist of a single character.


11. Build a program that reads four numbers between 100 and 999 from the keyboard and prints the largest number that is odd, divisible by three and that doesn't have an integer square root. If no such number has been provided, your program should print a message informing the user about it. In addition, if any of the numbers have more than three digits, your program should stop immediately, printing an error message. To find out if a number has an integer square root, compare its square root with the its own value, rounded:

>>> 100 ** (1/2) == round (100 ** (1/2)) True

Ex:
>>> strangeNumbers(200, 289, 153)
153
>>> strangeNumbers(997, 998, 999)
999
>>> strangeNumbers(100, 961, 121)
None of the numbers meets the established criteria


12. Build an even() function that takes three integers as parameters and returns an integer indicating how many of those are even.

Ex.
pairs (1, 5, 8) // returns 1
pairs (6, 8, 0) // returns 3
pairs (7, 7, 7) // returns 0


13. Build a longerString() function that takes two strings s1 and s2 as arguments. If the length of s1 is greater than that of s2, the function returns the number of additional characters s1 has in comparison to s2 and prints s1. If s2 is longer, it returns the number of additional characters of s2 and prints s2. If they are the same, simply return 0. For example:

>>> longerString ("abc", "de")
ABC
1
>>> longerString ("123", "456")
0
>>> longerString ("", "yeah")
yeah
4


14. Now create the intervalPlus() function which, given three numbers, a, b, and x, checks if x is less than a and b, greater than a and b, or if it is between a and b. In the first case it returns -1, in the second 1 and in the third 0.

>>> intervalPlus (10, 20, 10)
0
>>> intervalPlus (-9, 100, -10)
-1
>>> intervalPlus (0, 99, 187)
1


15. Build a program that, given the integer coefficients a, b and c, calculates the roots of the corresponding second degree (quadratic) equation (using the Bhaskara formula), if any. Remember to take into account the three possible cases: two real roots, one real root, and no real root.

>>> roots(3, 1, -1)
0.4342585459106649
-0.7675918792439983
>>> roots(2, -9, 0)
4.5
>>> roots(4, 5, 10)
No roots


16. Make a game of guessing the number. The game has two players. Player 1 inputs a secret number to be guessed. After that, that number disappears from the screen and Player 2 has three chances to guess the chosen number. For each attempt, the game must tell the player whether the guess is greater, less than, or equal to the secret number.


17. Build a printNumbers() function that takes a positive integer N as an argument and prints all the integers from 0 to it, including N. The function should check if N is, in fact, positive and, if not, should just print an error message and end.

>>> printNumbers(7) # single line or one line per number
0 1 2 3 4 5 6 7
>>> printNumbers(0)
0
>>> printNumbers(-10)
The provided number is negative.


18. Create a function that takes a number N as an argument and returns its factorial.

>>> fat(4)
24
>>> fat(10)
3628800
>>> fat(20)
121645100408832000


19. Build a function that takes a positive integer N as an argument and returns the sum of all numbers from 1 to N.

>>> summation(10)
55
>>> summation(24)
300
>>> summation(100)
5050


20. Build a function that takes a positive integer N as its argument and returns the sum of its digits, regardless of the number of digits.

>>> sumDigits(123456789)
45
>>> sumDigits(99999)
45
>>> sumDigits(10000000000000000000000000001)
2


21. You can also use for loops to cycle through the characters in a string. Build a lowercaseOnly() function that, upon receiving a text string as an argument, returns a string containing only text characters that are lowercase letters. For example:

>>> lowercaseOnly("aDDx2_ @ 2xef2n0)")
axxefn
>>> lowerCaseOnly("Fernando Castor")
ernandoastor
>>> lowerCaseOnly("1, 2, 3, 4! Yeah!")
eah


22. Build a function that takes an integer N as its argument and returns its integer cube root, if any. If not, the function must inform the user and return the number itself. Your program cannot use the potentiation operator ** or pre-existing functions in Python libraries to calculate the cube root. **It must be calculated iteratively**.

>>> iterCubeRoot(729)
9
>>> iterCubeRoot(1000000)
100
>>> iterCubeRoot(999)
No integer cube root.


23. Develop a prime() function that takes a positive integer as an argument and returns True if that argument is prime. If not, it returns False. The function should ascertain that N greater than or equal to 2.

>>> prime(729)
False
>>> prime(10009)
True
>>> prime(2)
True
>>> prime(9002)
False


24. A palindrome is a word or phrase that is read in the same way both in the traditional sense of reading and backwards. Examples of palindromes include "madam", "mom", "noon", and "racecar". Build a function called a palindrome that, given a word, determines whether it is a palindrome. For example:
>>> palindrome ("racecar")
True
>>> palindrome ("radar")
True
>>> palindrome ("belalugosi")
False

Your function should start by making the work use only lowercase letters. Use Python's lower() function for that.


25. Build a function called numPages() that, given the number of digits used to number the pages of a book, starting of page 1, determines how many pages the book has. For example, if the book has 11 pages (from 1 to 11), the number of digits is 13, because the book has 9 digits for pages 1 to 9 plus 4 for pages 10 and 11 Therefore, if your function is called with argument 21, you must return 15 because pages 1 to 9 have 9 digits and pages 10 to 15 add 12 digits (10, 11, 12, 13, 14, 15 - 1,0,1,1,1,2,1,3,1,4,1,5). A few more examples:
>>> numPages (13)
11
>>> numPages (21)
15
>>> numPages (192)
100
>>> numPages (1578)
562


26. Construct a primes() function that, upon receiving a positive integer N as its argument, prints all prime numbers between 2 and N itself. The function should ascertain that N greater than or equal to 2.

>>> primos(10)
2 3 5 7
>>> primos(30)
3 5 7 11 13 17 19 23 29
>>> primos(2)
2


27. A clerk named Dante works in a store where the cost of each item is a positive number of euro. In other words, an item can cost € 21, but nothing costs € 1.9. To give you change, this clerk has an unlimited amount of euro banknotes with the following values: € 1, € 5, € 10 and € 20. Build a function giveChange() that takes two parameters, corresponding to the cost of the item and the amount paid, and informs you how much change in terms of the quantity of notes needed using the least amount of bills possible. For example:

>>> giveChange (13, 50)
3 x € 10
1 x € 5
2 x € 1

>>> giveChange (40, 50)
1 x € 10


28. Make a program that, given a radius R, draws only using asterisks a circle (approximately) whose radius is R characters.
