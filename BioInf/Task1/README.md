# Find a Median String

***Task in [Rosalind #ba2b](https://rosalind.info/problems/ba2b/)***

*Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,*

$d(\textit{Pattern}, \textit{Text}) = \min\limits_{\text{all k-mers Pattern' in Text}}{HammingDistance(Pattern, Pattern')}.$

*Given a k-mer Pattern and a set of strings* $D_{na} =$ { $D_{na_{1}}, ..., D_{na_{t}}$ }*, we define* $d(Pattern, D_{na})$ *as the sum of distances between Pattern and all strings in* $D_{na}$ *,*

$d(\textit{Pattern},\textit{Dna}) = \sum\limits_{i=1}^t d(\textit{Pattern},\textit{Dna}_i).$

*Our goal is to find a k-mer Pattern that minimizes* $d(Pattern, D_{na})$ *over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for* $D_{na}$ *.*

**Median String Problem**

*Find a median string.*

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Given}$ : *An integer k and a collection of strings* $D_{na}$ *.*
 
&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Return}$ : *A k-mer Pattern that minimizes* $d(Pattern, D_{na})$ *over all k-mers Pattern. (If multiple answers exist, you may return any   
&nbsp;&nbsp;&nbsp;&nbsp; one.)*

**Sample Dataset**

> 3  
> AAATTGACGCAT  
> GACGACCACGTT  
> CGTCAGCGCCTG  
> GCTGAGCACCGG  
> AGTACGGGACAG

**Sample Output**

> GAC
