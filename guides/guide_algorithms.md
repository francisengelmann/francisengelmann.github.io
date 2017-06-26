# #############################################################################
# Hacking the coding invterview

## Coin Puzzle
Given 8 coins, one weights less, how many balances are needed?

## Processes/Threads
- mulitple threads access same memory
- multiple processes access separated memory

## Avoid Deadlocks
- first explain deadlock: two processes, two locks
- assign order to locks

## What is polymorphism?
ability of one method to have different behavior depending on 
- the type of object it is being called on
- the type of object being passed as a parameter. 

## Virtual function/method?
Allos subclasses to implement behavior of its on e.g.
	
	A * foo = new B(); // A and B implement bar()
	foo->bar(); // calls B->bar() if virtual in A, if not calls A->bar()

## Limitations atoi()
- if string too long, overflow can happen
- only works for specific input pattern, optional neg sign follow ed by digits

## return k-th element
- do pivot like quicksort, then only continue with one side
- O(n) = O(2n) = O(n) + O(n/2) + O(n/4) + ...
- same thing as finding MEDIAN!! k=n/2

## k-Nearest Neighbor
sort in O(n * log(n))
consider k previous and following neighbors
check this list 

## Cycle in Linked List
- two pointers, one slow, one fast, if they ever meet-> cycle

## Hash Function
- Find: O(1) expected (if has function is uniform), O(n) in WC
- suggest hash table while mentioning wirst case run time (to determine if interviewer likes hash tables)

## Anagrams datastructure
Given: *word* and a *list* containing all valid words
Find all permutations of *word* that are in *list*
- Build HashMap: sort each word alphabetically(=key), (word=value)
- Look up word in HashMap
	HashFunction: key of a value/word is the alphabetically sorted word

## Factorial Zeros
Number of zeros depends on how many times number is multiplied by 10.
- Count number of 5 in 100!

## Reorder list so that all reorders are equally likely
- Iterate over elements.
- Swap element with a random element from the remaining of the list.

## BST
insertion, removal, lookup are estimated O(log n) in a well balanced tree
o(n) in the worst case, if it is not balanced --> red black trees

## Path between nodes *OR* Lowest Common Ancestor
- exactly one path going through the lowest common ancestor

## BitWise Logic
15^12^15=12

## Compute 2^x quickly
res = 1 << x;

## Quick way of testing if number x is Power of 2
bool res = x & (x-1)
Idea: if it is, then there is only a single one!
4 = 100
3 = 011
4&3=000

## Beating the Stock Market
[1,2,3,5,2,4,8]
- iterate over the array
- track lowest stock price
- best deal so war (curr stock - lowest stock)

## Design Patterns
- Listener/Observer:
- Singleton: make sure exactly one instance of an object, no constructer but method getInstance()
- Model-View-Controller: used in GUIs

## Ransom Note
Input: Short String + Very Long String
Output: Whether it is possible to reconstruct Short String With Long String
- Iterate over short string
- Check in storage if current char is abailble
	- YES: decrease by one
	- NO: add chars from long string until found
- If we reach end of short string -> return YES
- If we reach end of long string -> return NO

## Coin Flipping and Die Rolls
- Generate random number between 1 and 6 using random number between 1 and 2
- First idea: use rand(1-2) to generate 3 bits, if result <=6 return, else repeat from beginning
- Other idea: fill a two dimensional array with continous numbers, first select one dimension, then second

## Target Sum
Input: x and [i,j,c]
two numbers add up to x?
- sort list O (n log n)
- pointer at start and beginning
- if sum is smaller, increase first pointer
- if sum is larger, decrease second pointer
- if two pointers meet, we cannot represent the number O(n)

## Valid BST
- it is not enough to check if left and right childs are valid with parents
- also check if they are in valid range of parent

## Find single occurance of variable
- keep sum,
- put all values into a set that are new, substract is value is already in set, else add to set and add to sum
- return sum
Better: just XOR ^ over all numbers, result is the single element

## Queue using two Stacks
Implement a queue using two stacks in and out
Idea: 	queue.push() - put all elements from out into in, then add new value
	queue.pop() - put all elements from in into out, then add new value

## Maximum subarray

# #############################################################################
# Algorithm Tricks

## Reverse container
reverse(res.begin(), res.end());

## Level Set Traversal
To keep track of levels, add NULL special node into queue

## Tree Traversal
*Queue* level set/ breadth traversal
*Stack* depth first traversal, inorder, postorder, preorder.

## stack and queue operators?
*front/back* for queues, double ended queue
*top* for stack, priority-qeueue
q.push(i); : push element at the end
int i = q.pop(); get front element

## vector constructor and initialization
vector<char> vc(10,'a');

## If order of input parameters makes a difference
string addStrings(string num1, string num2) {
        if (num1.size() < num2.size()) return addStrings(num2, num1);

## Comuting mean of two large numbers
int m = l + (r-l)/2;

## KMP Algorithm to find pattern in string

TODO: Find Google Problems from LeetCode
TODO: Solve Medium Difficult Problems
TODO: Solve Tree Problems
TODO: Solve Graph Problems

# Leet Code Questions

## First unique char in a string
* Initialize vector[26] to zero
* Iterate over all elements
* Increase element by one
* If letter occurs for the first time, add letter and its index to a queue<pair<char, int> >
* 
* Iterate over queue
* If count of letter is one, return its index (stored in the queue)

## Third maximum number
Add given array of numbers into priority_queue.
Pop two times, return head.

## Add strings
* Think of Addierwerk:
	- 3 inputs: 2 digits and 1 carry 
* Do not forget carry at the end

## Number of Segments in a String
* Count transitions from not" " to  " ".
* Add space as last letter, just to put it in a concise format.

## Reconstruct Original Digits from English
Input: "zeonreo"
Output "01"
* Count occurance of each letter in the input
* Iterate over all numbers and count how often in can be represented
* IMPORTANT: order of numbers: Zero, tWo, foUr, siX, eiGht, One, tHree, Five, seVen, nine 
 	put words with unique letters first to avoidone word stealing words from another
	put words in such an order that they can be identified with a unique letter (remaining of list)

## Island Perimeter
* Iterate over all fields
* Continue if it is water
* Check four directions whether border or water

## Reverse Words in a String
In place:
* Reverse the complete string
* Reverse words individually
Or first inversing indivual words, then inversing complete string

## Reverse Polish Notation
Idea: Use stack
* Check if operator using !isdigit() or number
* Push numbers on stack
* Take two top numbers from stack and perform operation
* Push result back onto stack
* return top stack element

## Battleships in a Board
Idea: count number of boat heads
* head = top and left is free

## Counting Bits
Idea: write down for a few examples and discover pattern
if i odd:  res[i] = res[i-1]+1
if i even: res[i] = res[i/2]

## Maximum Depth of Binary Tree:
Idea: recursive call, take max of depth(left,right)+1

### Same Tree
check wether two trees are the same
* First check if nodes are both empty or not
* If both nodes are not empty, check if they are equal
* If they are equal, check if left and right branches are equal recursively

### Lowest Common Ancester BST
Idea: easy because tree is sorted (binart search tree)
* compare to root key
* if both nodes are bigger then root, recursive call to right child of root
* if both are smaller, same on left

### Binary Tree Level Order Traversal
* Add sepcial signal NULL into queue to signal end of a level
* whenever we process a NULL, it means we have finished a line -> add a new NULL onto queue
Alternative: helper function with 2 parameter for level

### Balanced Binary Tree

### Kth Smallest Element in a Sorted Matrix

Add Digits
Happy Number
Sort Characters By Frequency
Sqrt
Spiral Matrix
Sum of Left Leaves
Rotate Array
Word Pattern
Pascal's Triangle
Word Search
Spiral Matrix II - solve this kind of problems
Valid Phone Numbers
Binary Tree Level Order Traversal II
Binary Tree Level Order Traversal
Symmetric Tree
Minimum Depth if Binary Tree
Binary Tree Right Side View
Binary Tree Zigzag Level Order Traversal
Minimum Height Trees
Maximum Depth of Binary Tree
Binary Tree Paths
Same Tree
Balances Binary Tree
Construct Binary Tree from Inorder and Postorder Traversal
Excel Sheet Column Title
Excel Sheets Column Number
Single Number - interesting one
Find Minimum in Rotated Sorted Array
Plus One
Convert Sorted List to BST
Reverse Linked List
Linked List Cycle
Remove Nth node From End of List
Spiral Matrix
Fizz Buzz
Nth Digit
Convert a Number to Hexadecimal

# Reverse String
* Iterate in while loop over half the string
* Use swap() to exchange them

# Reverse Vowels in String
* Iterate in while loop over string using find_first_of("aoeuv");
