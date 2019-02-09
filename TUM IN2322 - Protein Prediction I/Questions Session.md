# 1

### Explain the concepts of twilight zones

### Sequence - Sequence vs Sequence - Profile vs. Profile - Profile comparison. Why is Profile Profile more complicated?

For pairwise alignment, all that matters is the identity of the two letters that you currently compare. You compare letter by letter.

In a sequence profile comparison, you compare a letter here against a family. An entire family of related sequences. That is a vector essentially, you do number against vector comparison.

The tricky bit for profile profile comparison is that you have many alternatives for calling a vector vector pair a match or not -> complicated, a lot of free parameters that you have to optimize, unclear if they are optimal for ALL problems, they tend to be optimal for particular types of proteins, for example for proteins that have only alpha helixes or beta strands.

In the exam, you have to give two bullets or two examples or something like that.

### How do profiles help in the prediction of secondary structure?

Will clearly be asked! Will maybe coupled with another one. -> "Explain simple methods (1st generation, 2nd generation, 3rd generation methods) for secondary structure prediction"

- Profiles help because they contain more information (not sufficient alone)
- They contain more information because profiles are derived from families
- Allows you to see where are specific types of residues observed -> very informative for secondary structure (for example a region that only contains hydrophobic aminoacids will likely be in the center)
- Through the family you define what is relevant, you put the information in that is relevant
- Profile contain evolutionary information. Proteins evolve under constraints and the constraints are to maintain a 3D structure. This is why for the family that I see I have a constraint building. They tend to evolve such that the structure is maintained. That is very informative. If you just randomly chose sequences and put them in a family, that would not give any information. It only helps because you see something that has happened in nature -> what you see has survived under the constraint that structure has to be maintained. -> ML devices are able to pick up the signal out of the noise in the profile and extract the relevant information.

### What is the relationship between PSSM and profiles?
- PSSM and profile is the same thing
- Profile tells you at what particular position can you replace which residue by which other residue
- Blosum matrix only generically accounts for the biophysical features, regardless of position.
- PSSM also accounts for biophysical features but is also position-specific -> at this position, you need a hydrophobic residue, at that position, you need exactly this residue etc.

### What is the difference between BLAST and PSI-BLAST?
Will clearly be asked! But most likely as "What is the difference between DP and BLAST / hashing?" Typically, you do not have to write down the algorithm, just give them an idea of what the algorithm is.

Subquestion: After the first iteration, when we query the database, is this still BLAST? So is PSI-BLAST with only one iteration equals to BLAST?

- PSI -> Position specific iterative BLAST
- BLAST does pairwise comparisons
- PSI-BLAST builds up pairwise comparisons (queries the database and compares the given sequence with every entry using BLAST). In the next round, you're not using the sequence. Instead you replace the sequence by the PSSM and rund it against the database
- Int the first iteration, we move from pairwise alignments to aligning a sequence against a profile. We're taking every sequence from the database and align it against the profile. The second iteration does the same thing, but the profile is updated because we get more and more hits. You do it until nothing new is added to the hits.
- PSI-BLAST is therefore position-specific and BLAST is pairwise

### Is BLAST only the comparison method or also the process of comparing against a database?
- It is a program and when you run it, it compares against a database
- Originally, BLAST was just the pairwise comparison method
- BLAST is comparing sequence against a database
- BLAST is fast because you precompute the distribution of the database -> precompute, which sequences contain more than two of the query's seeds

### Whats the difference between Needleman-Wunsch and Smith-Waterman?
- Will not be asked in the lecture part of the exam
- Just expected to explain basic idea between DP the hashing type of BLAST. Why does BLAST speed up and how does it differ from DP
- Needleman-Wunsch 
  - DP gives you optimal answer provided you don't have gaps (?)
  - for global alignments
- Smith-Waterman 
  - is for local alignments and is pseudo-optimal
  - is the practical approach. in reality, you do smith-waterman. You don't do Needleman-Wunsch (introduced his algorithm before sequences were available)

### Do we allow gaps, when we talk about global alignments?
Yes, you allow gaps, otherwise it makes no sense. But then we arrive at Smith Waterman (?)  

### When do we want to use global alignments and when local alignments and why?
- Will be asked, will give fewer points
- Local always, global never
- Global alignment that for my search sequence, I know what I have in front of me, and it is the whole protein and hopefully a whole domain.
- Domain = subsequence that determines a unique 3D structure on its own
- Most proteins have multiple domains
- Global alignment would make sense if you take a protein domain by domain
- But most of the times, from the sequence alone, you don't really know what the domain is
- Expected answer: something about domains, say why it is difficult to know the unit of alignment (because proteins consist of multiple domains), global only makes sense if you have an entire domain and want you want to find is an entire domain
- Also expected: say what is global and what is local
  - Global: you align two proteins from one end to another
  - Local: you find some match
  - Show that with a figure!

### Why is it unpractical to do multiple alignments with DP?
- Ironic: one of the most frequently used programs to publish alignments / families in papers uses DP for alignments of multiple proteins
- Problem with DP is CPU time
- That program breaks down for 10,000 proteins (large family), for 1,000 it still works
- But that is what you need HMMs for, it is the much faster way of doing it
- There may be a question where it is helpful to know that HMM does alignments but not more
- Once you have the PSSM, Hammer's solution is as good as DP
- Question will probably not be asked. If anything, it will be part of another question

- If you talk about even just aligning 6 strictly with DP at the same time, then we're not talking only about CPU problems anymore. Then you need memory of multiple terabytes. 
- BLAST aligns a 1,000 proteins, the DP software also can do 1,000 and it uses hacks, such as the tree explained below.

### How many sequences do we know? How many structures do we know etc.?
- 120,000 known structures
- 120,000,000 known sequences
- 20,000 proteins in the human

### How do trees for multiple sequence alignments work?
- Relates to "Why is it unpractical to do multiple alignments with DP?"
Subquestion: which are the hacks for DP?
- Yes, there will be something like "What is a hack for DP?" or "How to do a tree ...?"

- You cannot compare 10 sequences with DP against each other at the same time
- So, what you do you compare them pairwise and then again pairwise of the results
- For pairs, you choose the most similar sequences as pairs
- For the result of a pair comparison, you have multiple alternatives, such as just taking the most probable residue or most informative
- Is a bit like a PSSM if you think about it
- The result is the consensus sequence. Problem: this is an artificial sequence and I still have not done the MSA! (mentioning this problem in the exam will maybe give points)
- Understanding of this will not be graded, basically just bullet points
- The better solution is a probability model, the tree is a hack, because biologist liked trees

### How does comparative modeling help us in predicting structure?
- Answer has to begin with: with comparative modeling, we can essentially model half of all the known sequences -> 60 million
- Then explain what comparative modeling is / how it works
- It works:
  - You have a query
  - You align the query against a database of proteins, for which you experimentally know the 3D structure (PDB)
  - Comparison is sequence-based -> Use alignment tools
  - Then you find a protein in the database as template, that is similar in sequence to the query
  - For instance in the daylight zone
  - Then you simply say that wherever they have a similar sequence, they have the same 3D structure -> You simply look up the 3D coordinates from the template wherever there is a corresponding residue
- Mention the zones! 
  - This is easier in some zones than in the other

- Will likely be a bigger question, where you have to know more about comparative modeling, for example where could it go wrong
- It can go wrong because you don't find a template / it is too much in the twilight zone / it is in the twilight zone and you make a mistake (false positive)
- Is there any way to recover from such mistakes? not really, there are some solutions for some issues -> Explain the issues

Why is it so easy to predict the structure?
- You don't have to predict anything
- You just copy the coordinates
- It's a bit more complicated because you then have to put the pieces together and deal with clashes, but it's still relatively easy

### How do we fill up the gaps (in the alignment) for our match when doing comparative modeling?

Will be asked

### For the consensus sequence, how do we choose, which letter to take from sequence A / B?
- Don't think about the consensus sequence, think about a probability model
- Two options: 
  - Choose the most likely model
  - Choose the most surprising model
- Two different solutions, but none of them gets it right
- Will probably not be asked

### What does hashing / BLAST do better than DP?
- This can be answered with bullet points
- It is about speed 
  -> You can do MSA with 100,000 (DP cannot do that)
  -> You can do all against all 120M against 120M (DP cannot do that, even complicated for hashing)
- Will be probably asked in connection with something else

### Describe an experimental method for measuring structure
- He will not ask us to describe in detail, how Xray crystallography works
- We should understand that the experimental structure determination is not trivial. They are structures that people are trying to get for 30 years and have not succeeded. Some of them are really difficult (membrane proteins). Even the easy structures take ~half a year and ~100,000 dollars
- We should know what the basic difference between Xray crystallography and NMR is
- Xray: get the proteins into a crystal and then shoot Xrays at it

### Why can you not see a protein under the microscope?
- It is too small and too dynamic

### What are tools for comparative modeling? How do they differ?
- Two tools for comparative modeling: Modeller and SwissModel
- Need to know very little detail
- Know some of the ideas / the problems underneath
- For example there are gaps that you need to bridge somehow
- There are regions that cannot be modeled
- Once you copy the coordinates of the aligned regions, what can go wrong? 
  - One thing is that you pick the wrong template. How can you find out about that? Well, when you have a lot of clashes
- This is what these tools are doing. For example, constraint satisfaction -> satisfying biophysical constraints

### What is disorder?
- Usually, a protein has a unique 3D structure in water, otherwise it would not be able to function correctly.
- In the last thing, this was put upside down, we talked about disorder. Disorder means the protein is adopting a unique 3D structure. At least, we have a region (the disordered region), whose 3D structure varies when I look at it at two different time points.
- One way to think about is that the information, what the protein will look like is 100% written in the sequence. But contrary to the usual "form a helix or a strand", now the information is "remain disordered" / "have a region that is disordered". 
- Upon binding, you suddenly adopt helical structure -> you order upon binding. The disordered region adopts to different locks -> it does not always have the exact same structure after binding, because it adopts to different proteins
- Another way of looking at it is that the 3D structure also contains information about where it is more flexible. Flexibility / dynamics is the way function is done. Dynamics are built into a structure.

### Where do we put the threshold for the b-values to decide whether a residue is flexible or rigid?
- Will not be asked
- Important to know: there are regions, which are more flexible than others
- You determine structure by turning the protein into a crystal. But when they are in their environment, they move, they are not static.
- Not even "what is a b value?" will be asked

### How do you encode a profile for a neural network?
- Different possible answers / ways
- Rather than one-hot encoding, just look at the probability vector at this specific position and put it in -> still a 21 dimensional input
- Probability vector could be a count (or a fraction so that it still sums up to 1)
- Another answer: you compile the degree to which this is surprising according to the BLOSUM matrix and put that into the neural network

### 2D contains almost the entire information of 3D
- From a complete distance map, you can compute 3D structure, except you cannot distinguish between the image and its mirror
- The question is then, how can we predict contact -> how can we predict 2D structure from a sequence
- ML is not really there yet. Can predict useful features, but not enough to predict 3D structure

# 2

### How can you predict per-residue secondary structure with a neural network? Explain in particular how to code for the sequence (keyword sliding window)
- Sliding window through the sequence
- Sliding window has input residue in the center! (obvious but don't forget)
- Input sequence is a sequence, for which you know the secondary structure
- Different ways of coding each amino-acid -> one-hot to prevent introduction of correlation between amino-acids. **Additionally** giving biophysical features helps.
- Training: sample by sample, slide the window through the sample
- Use spacer unit -> 21 input units instead of 20
- Don't actually slide the window through -> prevent correlation between subsequent input samples to the window. Put all these windows into a temporary database and then put input examples randomly into a batch. Otherwise, you push the network to much into one particular direction in space for each step

### What is the reason for a second level structure-to-structure network for predicting secondary structure? How much does this 2nd level improve over the 1st level (sequence-to-structure), and what IS the 1st level?
- Problem with only 1st level is that the system never learns that for example helices have to have a minimal length (3 to 4 residues long)
- Take output from 1st level as input to 2nd level
- Again, add a spacer unit
- Train separately
- 2nd level can learn that isolated Hs (without a helix) are very rare -> make HOH to HHH

How do you measure secondary structure prediction?
- Q3 measure
- Improves the "makes sense" of the prediction -> predicts a much more realistic length distribution (for helices)

### Applying a method for secondary structure prediction fails for proteins with transmembrane helices (TMH). How could you adapt the known solution to the new problem?
- Retrain with new data, but now you use data from membrane proteins
- Again with 1st level and 2nd level. Again 1st level predicts transmembrane helices too short. But now, the 2nd level makes them much too long.
- Hack for this: Cut (more in the lecture) -> PHDhdm
- Sequence runs from left to right. At the top, three helices shown by red and white striped boxes. Now, you see numbers: 5, 30, 6, 5. The idea is that these stand for the number of positive charges in the region left of that box. So before the first box, there are five positively charges residues. R and K are positive charges. Ignore 5, 6, 30
- Sum = 2 of R and K. In the next loop (part between the helices / boxes), there are 5 R and Ks. Then there are 3 and then there is 1. Positive inside means that the part of the protein that is on the inside, there are more positively charged residues.
- Now the question is: how do i have to arrange the loops such that the numbers add up such that at the inside, i have more positive charges? the answer is shown for the bottom. this is the only way in which you can do it.
- The positive inside rule is to determine the orientation of the helices -> is the first part of the protein on the inside or on the outside - that is the problem.
- That is relevant because (it is referred to as the topology) and the topology of a protein is essential for understanding its function. -> understand proteins of similar function. Everything with which we sense things (smelling for example) they have always the same number of 7 helices and the same orientation.
- The helices are given! You look at everything that is in between the helices. 
- Essentially, you sum over all even loops and over all odd loops and decide which ones are inside and which ones are outside

How do you cut helices? Helices have a minimal and a maximal length. They are say 15 to 25 residues long. Otherwise, they cannot go through the lipid. 
- You simply let the neural network predict T (transmembrane residue) or N for each residue. 
- Then, you can fit transmembrane helices
- -> Gives you several possible transmembrane helices (top right black / blue figure)
- -> Assign the average T-probability value per residue to each helix
- -> Now, you go through k = 1 to maximal found helices and pick the k most likely helices (based on their average T-probability). 
- -> Now, you have to decide, which k-Model is best. Again, use the T-probabilities, and say the probability of having three is more likely than having two, for example, because this helix in the middle would otherwise have to turn to N (if it were only two helices).
- -> Sum over the values for all residues for each k-model 

### How does PROFsec even improve the predictions? Which kind of methods are added to improve?
- Was covered in q1.txt

### Difference between alpha-helix and beta-strand
- Will not be asked

### Profiles improve the prediction of protein secondary structure. Given two multiple alignments for a family, how can we assess which one is better (assume these two exist for proteins for which you know the secondary structure; suggest one way to check)? How can you find the better of two if you do NOT know the secondary structure? What aspects of the alignment are relevant to improve the prediction?
- Has a short answer: which ever one has the lower validation score -> which one predicts better
- If you don't have the secondary structure, check the reliability index (this answer is not enough)
- Also explain what the RI tells you -> if it is low, then what? if it is high then what?

What would be things that make the prediction based on the profile better?
- That is again the question of q1.txt why are profiles nice?

What makes the profile better?
- More sequences
- Sequences of similar length
- Sequences stemming from the same family
- Varying sequences -> not always the same sequence -> more diversity
- Three important features in the Alignment:
  - number of sequences
  - diversity
  - same family / contains no alignments of unrelated proteins -> to check that, just predict secondary structure for the sequences. If some are alpha helices, some are beta strands you see that some thing is wrong (this method is slightly circular)

### What is the reliability index?
TODO

### Why is secondary structure prediction not robust to disorder?
Prof answer: it is

### Give an example for a method that predicts protein disorder through machine learning without using any experimental data about disorder. This method uses no positive (disorder) “like” what it is supposed to predict and uses many negatives (not disorder) that incorrectly labelled. How can it still work? 
- Protein disorder is a phenomenon that we cannot see directly by any experimental means
- Task is to find regions of 30 in a dataset that contains nothing shorter than 70
- Neural network can find what is the consistent signal and completely ignore the errors in the ...

### For secondary structure prediction there are neural network trained in “balanced” and in “unbalanced” fashion? What is the difference? What is the advantage of “balanced”, what the disadvantage? Why could it help to compute a “jury” (average) over balanced AND unbalanced? What type of error can be improved by averaging over many methods?
- Answers in the lecture
- First statement:
- The jury improves because it reduces the white noise. It reduces the random mistakes the networks make.
- Averaging over two different methods always helps, when there is white noise
- Both prediction methods have an advantage -> combine the best of both worlds
- Disadvantage of balanced training is the performance decrease
- Balanced means, that you repeat the rare classes a lot
- Weighing of samples is often used for unbalanced data, but this does not work here
- Important answer here: it depends on how you measure performance! (test data balanced or accuracy per class)

### Define five different criteria to measure the performance of secondary structure prediction

### You have method A and method B. Method A performs this way, method B that way. What can you say, what can you not say? What kind of questions do you need to ask?
- Definitely in the exam!

### Statistical significance? What are statictically siginificant digits? What data set size is relevant? Standard Varianz?
- Will definitely be asked

### What is the positive-inside rule? How can it be used to improve transmembrane helix (TMH) prediction?
- Short question, short answer

### Why do we need more “global” information for the prediction of beta-strands than for alpha-helices? Answer what most people (as e.g. represented by Wikipedia) believe. What did you learn in the lecture that tells you that this answer is incorrect?
- Through balanced training, you can predict both equally well. The only way where that can happen: 
- It is true that formation of beta strands is done by long-ranging interactions. The propensity for the formation of beta strands is equally strong when compared with the one for helices for a sliding window of 13, although beta strand formation is global.


### How can you use the amino acid proline to predict helices?
- Will be asked

### UCON, NORSnet, MetaDisorder - how can we predict disorder? - Do we have to know about these methods?
- You don't need to know the acronyms
- What is helpful to know is what is it that you need to do in order to predict disorder
- One method stands for disorder has to do with long loops
- One method stands for disorder has to do with low contact density -> very few residues bind to other things -> If you have something that has a low of constraints, it cannot have disorder -> this is UCON
- MetaDisorder is a ML device. If you explain this, you need to explain, where you get the data from. What type of data and how you can use it etc.

### General
- Nail it!
- Figures are more clear and easier to read for them
- There will be less questions with more points
- They try to design the exam so that you can show that you understood. But with 300 students it will be bullet points
- Multiple choice at the beginning
- They will avoid questions like "Explain ..."
- Questions will have their number of points next to them. Few points -> bullet points
