Advent of Code Day 1 2024: 
*   list of numbers are in the text file, 
*   and my python code to solve it, aoc_day1.py.


I used both **sorted** the built in python method as well as **quicksort**.

This was a pretty simple solution, just required a bit of thought to get to the right answer.
The two best tools I use are the debugger and the print statement. I used the debugger to step through the code and see what was happening at each step. I also used the print statement to see what the values of the variables were at each step. This helped me to understand what was going wrong and how to fix it.

Advent of Code Day 2 2024 - 

Using the debugger was big for part two as I wanted to do it differently.  Also, one issue I ran into was when parsing the input, I was trying to strip and split the input into their own lists and then convert to integer.  However, because the last character in the input was a newline, that would be parsed to an empty string, which I could not strip.  I could have used **rstrip** and cut everything off before the new line and that would have been one way.


I might still use rstrip as as another way to do it.  One thing I noticed while debugging was that the input was being broken up fine.  So I would take in the text file and split it to a list of lines, then split that to be a list of integers.  At first I wanted to just get it over with so I tried to just use functions.  Eventually I made it a class and had to rework the logic a bit, but it overall made it easier to read and understand.  When I did this though I realized that I was setting the answer, so any calculation I did was not being saved.  Then I also realized the logic wasn't working as it had prior to making a class.  Even though I kept that logic the same, it was not evaluating them correctly, instead they were all coming out as safe.  Prior each time it had always realized when it was off the pattern.  I went through the debugger and saw it myself.  However, when I evaluated the logic as a class, it did not work, which allowed me to simplify it a bit.  I had also then realized yes I was doing this the simply way, I could be using more advanced functions.  However, I think this is the best way to understand what is going on, as a lot of advanced functions do the heavy lifting for you.

I also have redundant logic solving the problem in two ways, essentially checking myself.  As turning it into a variable makes it cleaner, but you cannot use it everywhere.  I also have print statements which helps to understand what is going on as well as debug it.  I think it will also help anyone who wants to understand what I did, or anything.  The logic is not difficult to understand, it is not hard to do, it takes planning and a thought out process.  It's not complicated code or anything really, and if you think about it, this is similar logic to what you do in any advanced algorithm.  The types can be hard to understand when you are getting issues, and it can be hard to think through, so using the debugger simplifies it.

I also had realized that I had read the problem wrong, originally I had it set for 2 or less, and it was 3 or less.  So is gradually increasing or is gradually decreasing.  I plan on working these through and refactoring the code to be cleaner and more efficient.  I also plan on adding more comments to the code, as I think it will help anyone who wants to understand what I did, or anything.  I also left the print statements I used for debugging like I said, and both methods arrive at the same answer.  Advent of Code Day 2 2024 Done.

I used numpy to turn the list into an array, and then I used numpy diff to create a
list of differences.  Once I had the list of differences, I could compare to make sure
they were all decreasing or increasing.  Numpy was much easier obviously, but the logic works for both.

