# Reconstruct a String from its Paired Composition 

***Task [Rosalind #ba3j](https://rosalind.info/problems/ba3j/)***

Since increasing read length presents a difficult experimental problem, biologists have suggested an indirect way of increasing read length by generating **read-pairs**, which are pairs of reads 
separated by a fixed distance d in the genome.

You can think about a read-pair as a long "gapped" read of length k + d + k whose first and last k-mers are known but whose middle segment of length d is unknown. Nevertheless, read-pairs 
contain more information than k-mers alone, and so we should be able to use them to improve our assemblies. If only you could infer the nucleotides in the middle segment of a read-pair, you 
would immediately increase the read length from k to 2 · k + d.

Given a string Text, a **(k,d)-mer** is a pair of k-mers in Text separated by distance d. We use the notation $(Pattern_{1}|Pattern_{2})$ to refer to a a (k,d)-mer whose k-mers are 
$Pattern_{1}$ and $Pattern_{2}$. The **(k,d)-mer composition** of Text, denoted $PairedComposition_{k,d}(Text)$, is the collection of all (k,d)- mers in Text (including repeated (k,d)-mers).

**String Reconstruction from Read-Pairs Problem**

Reconstruct a string from its paired composition.

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Given}$ : Integers k and d followed by a collection of paired k-mers PairedReads.

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Return}$ : A string Text with (k, d)-mer composition equal to PairedReads. (If multiple answers exist, you may return any one.)

**Sample Dataset**

>4 2  
>GAGA | TTGA  
>TCGT | GATG  
>CGTG | ATGT  
>TGGT | TGAG  
>GTGA | TGTT  
>GTGG | GTGA  
>TGAG | GTTG  
>GGTC | GAGA  
>GTCG | AGAT

**Sample Output**

>GTGGTCGTGAGATGTTGA
