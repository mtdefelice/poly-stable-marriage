# poly-stable-marriage

A polygamous stable marriage implementation in Python. Based on the [Gale–Shapley algorithm](https://en.wikipedia.org/wiki/Stable_marriage_problem).

## Output

```
$ python3 psm.py 
On John
Trying Org. Org_B
John is now tentatively interning at Org_B.
On George
Trying Org. Org_H
George is now tentatively interning at Org_H.
On Lucy
Trying Org. Org_F
Lucy is now tentatively interning at Org_F.
On Rita
Trying Org. Org_A
Rita is now tentatively interning at Org_A.
On Paul
Trying Org. Org_B
Org_B seems taken.
The Org. is happier with John vs. Paul.
Trying Org. Org_E
Paul is now tentatively interning at Org_E.
On Michelle
Trying Org. Org_B
Org_B seems taken.
The Org. is happier with John vs. Michelle.
Trying Org. Org_D
Michelle is now tentatively interning at Org_D.
On Ringo
Trying Org. Org_C
Ringo is now tentatively interning at Org_C.
On Pam
Trying Org. Org_E
Org_E seems taken.
Pam Appears to be a better match for Org. Org_E than Paul.
On Paul
Trying Org. Org_B
Org_B seems taken.
The Org. is happier with John vs. Paul.
Trying Org. Org_E
Org_E seems taken.
The Org. is happier with Pam vs. Paul.
Trying Org. Org_D
Org_D seems taken.
The Org. is happier with Michelle vs. Paul.
Trying Org. Org_A
Org_A seems taken.
The Org. is happier with Rita vs. Paul.
Trying Org. Org_F
Org_F seems taken.
Paul Appears to be a better match for Org. Org_F than Lucy.
On Lucy
Trying Org. Org_F
Org_F seems taken.
The Org. is happier with Paul vs. Lucy.
Trying Org. Org_B
Org_B seems taken.
Lucy Appears to be a better match for Org. Org_B than John.
On John
Trying Org. Org_B
Org_B seems taken.
The Org. is happier with Lucy vs. John.
Trying Org. Org_G
John is now tentatively interning at Org_G.
```
