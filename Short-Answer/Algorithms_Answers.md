# Analysis of Algorithms Answers

## Exercise I

a)

```python
    a = 0                       | O(1)
    while (a < n * n * n):      | O(4)
        a = a + n * n           | O(3) = O(8) = O(1)
```

This algorithm runs eight operations no matter how large n is. I'd call that O(1), constant time.

-----------------------------------------------------------------------

b)

```python
    sum = 0                                    | O(1)
    for i in range(n):                         | O(n)
        i += 1                                 | O(1)
        for j in range(i + 1, n):              | O(n - i + 2) = O(n)
            j += 1                             | O(1)
            for k in range(j + 1, n):          | O(n - i + 2) = O(n)
                k += 1                         | O(1)
                for l in range(k + 1, 10 + k): | O(10) No matter what k is, always loop 10 times
                    l += 1                     | O(1)
                    sum += 1                   | O(1) = ?
```

From my understanding, you multiply loops by the body. So on line 27, we see that no matter what k is that loop will always run 10 times. And it has two operations in its body, so you'd multiply 2 and 10.

If you look at line 25, you see that's an O(n) loop. For each iteration, you'd multiply by the body, which is O(1) + O(20), so O(21n) or just O(n) after you drop the constant 21.

My final analysis is that this is O(n^3), which is not good.

### I based my argument on what Beej says in this video.

[![Beej talking Big O](https://lh3.googleusercontent.com/Ned_Tu_ge6GgJZ_lIO_5mieIEmjDpq9kfgD05wapmvzcInvT4qQMxhxq_hEazf8ZsqA=s180)](https://youtu.be/JOOkFhkeL38?t=3216 "Click to see what I'm basing my argument on")

-----------------------------------------------------------------------

c)

```python
    def bunnyEars(bunnies):                |
        if bunnies == 0:                   | O(1)
            return 0                       | O(1)
        return 2 + bunnyEars(bunnies-1)    | O(n) 
```

I'd call this algorithm O(n), where n is equal to the number of recursive loops it would run until bunnies is equal to zero. 

-----------------------------------------------------------------------

## Exercise II

This is a perfect case for binary sort.

1) Our floors are without a doubt sorted already. It would be a strange situation if the floors weren't already sorted. That's kinda how floor numbering works, the value of the floor is determined by where it is in relation to the ground. So that's good.
2) So with a sorted list of floors, we can just divide the number of floors by half(rounded up), and check that number floor by dropping an egg.
3) If the egg breaks, we know we're too far from the ground. Floor _f_ must certainly be one of the floors below.
4) If the egg does not break, we know that floor _f_ must either be this floor, or one of the floors above.
5) We've ruled out half of the possibilities already in our first egg drop. Next, we'll divide the remaining half of possibilities in half and repeat the process.
6) Keep dividing the remaining possibilities in half and checking that floor until you narrow it down to one floor. 
