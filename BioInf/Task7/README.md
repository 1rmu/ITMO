# Implement the Viterbi Algorithm

***Task in rozalind.info #ba10c***

**Decoding Problem**

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Given}$ : A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix   
&nbsp;&nbsp;&nbsp;&nbsp; Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

&nbsp;&nbsp;&nbsp;&nbsp; ${ \color{green} Return}$ : A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.

**Sample Dataset**

> xyxzzxyxyy  
> \-\-\-\-\-\-\-\-  
> x   y   z  
> \-\-\-\-\-\-\-\-    
> A   B  
> \-\-\-\-\-\-\-\-  
>     &nbsp;&nbsp;&nbsp;&nbsp; A  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; B  
> A   0.641   0.359  
> B   0.729   0.271  
> \-\-\--\-\-\-\-  
>      &nbsp;&nbsp;&nbsp;&nbsp; x    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; y    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z  
> A   0.117   0.691   0.192  
> B   0.097   0.42    0.483

**Sample Output**

>AAABBAAAAA
