# Find a Shortest Transformation of One Genome into Another by 2-Breaks

***Task [Rosalind #ba6d](https://rosalind.info/problems/ba6d/)***

**2-Break Sorting Problem**

Find a shortest transformation of one genome into another by 2-breaks.

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Given}$ : Two genomes with circular chromosomes on the same set of synteny blocks.

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Return}$ : The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into   
&nbsp;&nbsp;&nbsp;&nbsp; the other.

**Sample Dataset**

> (+1 -2 -3 +4)  
> (+1 +2 -4 -3)

**Sample Output**

> (+1 -2 -3 +4)  
> (+1 -2 -3)(+4)  
> (+1 -2 -4 -3)  
> (+1 +2 -4 -3)
