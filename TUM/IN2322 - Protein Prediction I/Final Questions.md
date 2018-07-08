# Q1

### Explain the concept of twilight zones
- When aligning sequences (for example with BLAST), we get a score for the sequence similarity
- From sequence similarity, we may be able to infer the structure. But this does not necessarily have to be the case!
- It is therefore hard to interpret the alignment score
- We can run all vs. all sequence alignment on PDB. For each pair, we can plot the sequence similarity (x-axis) and check, if the two proteins also have a similar structure.
- Plot
- This leads to the following zones (TP are defined as pairs that have similar sequence and similar structure, FP as similar sequence and different structure):
  - Daylight Zone: 
    - TP > FP 
    - two proteins have a similar structure
    - do sequence - sequence comparison
  - Twilight Zone: 
    - TP increase, but FP explode -> FP > TP
    - can't reliably predict structure from sequence
    - do sequence - profile comparison
  - Midnight Zone:
    - FP >> TP
    - no significant prediction ability
    - do profile - profile comparison
    
### Sequence - Sequence vs Sequence - Profile vs. Profile - Profile comparison. Why is Profile Profile more complicated?
- For pairwise alignment, you simply compare letter by letter using the score matrix
- For sequence - profile comparison, you compare letter against a family of related sequences  
  -> essentially a vector  
  -> number against vector comparison
- For profile - profile, you need a way for calling a vector vector pair a match 
  -> many alternatives 
  -> many free parameters that need optimization
  -> parameters tend to be optimal only for particular types of proteins (for example that have only helixes)
  
### How do profiles help in the prediction of secondary structure?
- Profiles contain more information, because they are derived from families, which are a result of evolution.  
  -> Profiles contain evolutionary information. Proteins tend to evolve such that the structure is maintained. Evolution only shows us what survived, so it shows us for each position, which residues are possible without changing the structure.
- They show us where specific types of residues are observed
  -> very informative for secondary structure. for example, a region that only contains hydrophobic aminoacids will likely be in the center
- ML devices are able to pick up the signal out of the noise in the profile and extract the relevant information

### Why is PSSM better than BLOSUM?
- Profile tells you at what particular position you can replace which residue by which other residue
- Blosum matrix only generically accounts for the biophysical features, regardless of position
- PSSM also accounts for that but is also position specific -> at this position you ne a hydrophobic residue, at that position, you must have Alanine etc.

### What is the difference between DP and BLAST / hashing?
- Speed! 
- BLAST can run alignment queries against a database (to search for similar sequences) much faster 
- DP breaks down for aligning large families, for example 10,000 proteins. BLAST can handle that by using hashing.
- BLAST can even handle 10M against 10M alignments

### What does BLAST do?
Searches a database for similiar sequences by doing pairwise comparisons
Key element: use seeds for hit determination
1. Search for seeds in the query -> 3-grams that have a high alignment score at some position of the query
2. Search database for hits  
   -> already has stored, which seeds are contained in each entry
   -> return sequences that contain at least two seeds 
3. Expand the regions, where the seeds of the query and hit match, by using local alignment (DP is much faster now, because only done on small part of the sequence)
4. Return the locally aligned sequences 

### What does PSI-BLAST do?
Builds up pairwise comparisons in order to create a PSSM and expand the hits
1. Run BLAST with BLOSUM as score matrix
2. Build PSSM based on the high-scoring hits
3. Search again, but this time using the PSSM -> use profile instead of sequence
4. Repeat 2 and 3 until convergence

### Whats the difference between Needleman-Wunsch and Smith-Waterman?
NW:
- global alignments
- DP gives you optimal answer provided you don't have gaps
- unpractical because you assume that what you have in front of you is exactly one domain
SW:
- local alignments
- pseudo-optimal
- practical approach

### When do we want to use global alignments and when local alignments?
- Global means aligning two proteins end to end
- Local means you find some match
- Figure
- Global alignments are only suitable, when the assumption is that the two proteins only consist of a single domain
- This is a strong assumption, less than 30% of the proteins have a single domain
- Also global alignment breaks, if one sequence is only a part of a protein
- -> Hard to know the unit of alignment
- -> In practice, use local alignment

### Why is it unpractical to do multiple alignments with DP?
- Strictly using DP on only 6 sequences will already take terabytes of memory  
  -> not feasible
  -> hacks needed, such as trees / probability model
- Even with hacks, the problem is CPU time
- DP works for aligning 1,000 proteins but breaks down for aligning large families (10,000 proteins)

### How many sequences do we know? How many structures? How many proteins in a human?
- 120,000,000 sequences
- 120,000 structures
- 20,000 proteins in a human

### What are the hacks for DP?
- DP runtime for 2 sequences is O(length^2). For 3 it is O(N_1 * N_2 * N3)
- -> You cannot compare 10 sequences with DP against each other at the same time
- Compare the sequences pairwise and then compare the results pairwise again to reach a consensus sequence
- Builds binary tree for example
- Needs method for deciding which letter to take
  - Take the most probable residue
  - Take the most surprising residue
- Result is a consensus sequence
- Problem is that given the consensus sequence, we still don't have the exact alignment for the original sequences. The consensus sequence is artifically created! 
- Better: build a probability model accounting for all amino acids

### How does comparative modeling help us in predicting structure?
- 60 million proteins possible to (at least partially) predict with comparative modeling!
- Steps:
  1. You have a query (target)
  2. Align the query against a database of protein, for which you **experimentally** know the 3D structure (PDB)
  3. Use alignment methods for sequence to sequence comparison
  4. Find a protein with high sequence similarity as template (should optimally be in the daylight zone)
  5. Take the 3D coordinates from the template and fill them with the target according to the alignment
  6. Assess and refine the model
  7. Problem: What to do with gaps in the alignment?

### When can comparative modeling go wrong?
- When you don't find a template
- When the template is a false positive (likely if too much in the twilight zone)
- When there are gaps in the alignment, but there are solutions to this
- Mis-alignment breaks the prediction

### How can you find out that you picked the wrong comparative modeling template?
You have a lot of clashes.

### Why is comparative modeling so easy?
- Don't have to predict anything
- Just copy the template coordinates
- Is a bit more complicated, because you have to deal with gaps / clashes but still relatively easy

### What are solutions to gaps in the alignment when doing comparative modeling?
- Gap = target sequence has additional residues inserted in comparison with template
- You need to predict the structure between the two "anchor" points:
  - Molecular simulation
  - Search database for loop sequence and infer its structure

### What are methods for experimentally determining structure?
- Xray crystallography
- NMR = Nuclear Magnetic Resonance

### How does Xray crystallography work? How many known structures resulted from it so far?
- 90% of 120,000 structures
- Get protein to form a crystal
- Shoot Xrays at it -> diffraction pattern
- Infer the structure by fitting a model

### How does NMR crystallography work? How many known structures resulted from it so far?
- 9% of 120,000 structure
- NMR = Nuclear Magnetic Resonance
- Put proteins from their environment into a tube -> proteins don't have to be modified!
- Put the tube under a large magnet
- Measurements only give constraints -> Models have to be fitted -> Several models as output that are compatible with the data -> is uncertain -> might be due to dynamic regions of the protein (b factors)

### Why can you not see a protein under the microscope?
It is too small and too dynamic

### What are tools for comparative modeling? How do they differ?
- Modeller and Swiss-Model
- There are gaps from the alignment, that you need to bridge somehow, because you can't take the structure from the template
- -> There are regions that cannot be modeled
- Modeller:
  - very accurate
  - more complex -> for experts
- Swiss-Model:
  - simply find template with BLAST / PSI-BLAST and copy the coordinates
  - for non-experts

### What is disorder?
- Usually, proteins have a unique 3D structure in water, otherwise they would not be able to function correctly
- Disorder = at least a part of the protein is not adopting a unique 3D structure 
- -> When looking at it at two different times, it does not have the same structure
- What the protein will look like is still written 100% in the sequence. It is just that what stands there is not "form a helix or strand" but now the information is "have a region that is disordered"
- Upon binding, it adopts structure -> orders upon binding
- Adopts to different locks with different structure
- Flexibility and dynamics enable its function

### How can you encode a profile for a neural network?
- Instead of one-hot encoding:
  - Can also input the row of the PSSM -> input still 21 dimensional (with spacer unit)
  - Or input the corresponding probability vector -> input still 21 dimensional, still sums to 1
  
### Why don't we predict the 2D distance map?
- From that, you can directly compute the 3D structure (except for image <-> mirror distinction)
- Would need to predict contact of residues
- ML is not there yet. Can predict useful features but not enough to predict 3D structure

# Q2 

### How can you predict per-residue secondary structure with a neural network? Explain in particular how to code for the sequence.
- Sliding window through the sequence with residue to predict secondary structure for at the center
- Figure
- Training input sequence is a sequence, for which you know the secondary structure
- One-hot encoding of aminoacids at each position -> does not introduce correlation between aminoacids like putting in the binary code with only 5 input units would
- Train sample by sample, slide the window through the sample 
- Don't actually slide the window through! Pre-compute the (input, output) pairs, put them into the database and then iterate them randomly
- Use a spacer unit -> 21 instead of 20

### What is the reason for a second level structure-to-structure network for predicting secondary structure? 
- Problem with only 1st level is that the system never learns for example that helices are at least 3 to 4 residues long or HLHL does not exist
- Take output from 1st level as input to 2nd level
- Again, add space unit
- Train after the 1st level
- Still only 60% accuracy!

### Applying a method for secondary structure prediction fails for proteins with transmembrane helices (TMH). How could you adapt the known solution to the new problem?

TODO

### Given two multiple alignments for a family, how can we assess which one is better?
- If you have the secondary structure: Which ever one has the lower validation score -> which one predicts better
- If not: check the reliability index
- If it is low, then TODO
- If it is high, then TODO

### What is the reliability index?

TODO

### What contributes to a better profile?
- More sequences
- Sequences of similar length
- Sequences stemming from the same family -> no unrelated proteins in the MSA
- Diverse sequences -> not always the same sequence

### How can you check that there are no unrelated sequences in the MSA for your profile?
- Build the profile
- Predict secondary structure for the sequences in the MSA
- If some are alpha helices and some are beta strands -> something went wrong

TODO TODO


### Explain simple methods (1st generation, 2nd generation, 3rd generation methods) for secondary structure prediction

1st generation:
- Proline breaks a helix
- Take all proteins with known structure and convert them to 1D with DSSP
- Count the secondary structure states for each amino acid for each protein and build a probability distribution for each amin-acid
- Assign single secondary structure label to each amino-acid (simply take the most frequent one)
- From 50s to 70s
- Around 50% accuracy

2nd generation:
- Also look at the window (segment) instead of just one aminoacid
- Pad start and end with additional spacer unit
- Again, count the secondary structure labels for each segment combination

3rd generation:
- Use neural network with 2 levels
- Also encode profile

# Exercise Questions

### Fat, water, loving, hating?
- Hydro
- Lipo
- philic
- phobic

### What is the central dogma of Molecular Biology?
1. DNA Replication
2. Transcription to RNA
3. Translation to Protein

### What is an ORF?
- Open Reading Frame
- DNA sequence that precisely codes for a protein
- DNA sequence consisting of start codon encoding M, intermediate codons, stop codons (not encoding)
- In exercises: 1 ORF = 1 protein, but 1 -> N proteins is also possible

### Where do 6 reading frames come from?
- 3 for different start positions
- 2 for complementary strand

### What is special for ORF for complementary strand?
Read in reverse -> always from 5 to 3, but these numbers flip when taking the complement -> have to reverse reading

### What is the central file format?
>FASTA
asdf
1234

### Why do we want to align sequences?
- Find out how similar they are
- Similar sequences tend to have similar shapes -> Make conclusions about structure and function
- Observe patterns of conservation
- Infer evolutionary relationships

### Name two databases for proteins
- UniProt for protein sequences
- PDB for protein structures

### What is a high-level description of DP in general?
- Divide a problem into consecutive subproblems
- Solution for each problem is based on its predecessors

### How does Needleman-Wunsch work?
1. Matrix with rows and columns = the sequences
2. Insert additional row and column at index 0 and insert 0 at 0,0
3. Fill first row and column using gap penalty
4. Take score matrix and gap penalties
5. For each entry, take max(top left + score, top + gp, left + gp)
6. Go back from the bottom right cell using cell that check out 
7. Save all possible paths to get all possible alignments

### How does Smith Waterman work?
- Matrix cell values are always >= -> fill first row and column with zeros
- Start traceback at cell with max value and go back to cell with 0 value

### What are the steps in computing a PSSM?
1. Calculate sequence weights
2. Count (with weights) observed amino acids and gaps
3. Redistribute gaps according to background distribution
4. Add pseudocounts according to amino acid pair frequencies
5. Normalize to relative frequencies
6. Divide by background frequencies
7. Calculate Log-Score
8. Remove rows corresponding to gaps in the primary sequence (first one in the MSA)

### Why do we want PSSMs?
1. Help improve alignments (local and global) -> Instead of BLOSUM62
2. Can be used for search of similar sequences (for example for BLAST)
3. Condense information about the evolution of a protein -> Important input feature for many prediction methods
4. Help to find protein homologs in database

### What is a problem of PSI-BLAST?
False hits can pollute the PSSM

### What is an advantage of PSI-BLAST?
Can find more distantly related protein sequences.

### What is the typical ML workflow?
1. Preprocessing
2. Data Analysis
3. Model training
4. Performance evaluation

# Introduction

### What are the nucleotides of DNA and RNA?
- ACGT
- ACGU

### How do you get from DNA to a protein?
- Codon of 3 nucleotides for one amino acid

### What is the difference between eukaryotes and prokaryotes?
Eukaryotes have a nucleus

### What is the length of the shortest and the longest protein?
35 to 35K residues

### What are the two parts that make up an amino acid?
- Side chain (different for each amino acid)
- Backbone (same for all amino acids)

### What are some biophysical features?
- Polar
- Hydrophilic
- Hydrophobic
- Positively charged
- Negatively charged

### What is an intron? What an exon?
- Intron is a DNA region that is cut out -> not used to build proteins
- Exon is a DNA region that is used (given that it is between the start and end codon)

### What is a domain?
- A sequence of residues that folds independently of other sequences in the protein
- A protein can have multiple domains
- < 30% have a single domain
- Domains often contain evolutionary information -> different proteins have the same or a similar subsequence with the same structure

### Why would evolution decide to merge two protein (domains)?
- Because protein A and B have to act together -> have to bind locally together
- By constructing C = A + B, the proteins don't need to meet anymore
- -> Join these sequences in the genome to save time

### Why do we compare the sequences instead of 3D structure?
- For most proteins, we don't have the 3D structure (Only for 120K proteins)
- Also, comparing sequences is easier
- 3D structure comparison would be better, because the structure does not have to be similar for similar sequences

### How can we compare 3D shapes?
With 2D matrix comparison
1. Find the best global superposition (points where both shapes are the closest)
2. Compute for each shape the distance matrix between its points (isolated from the other shape)
3. Compare both matrices -> RMSD 
Can also compare matrix subregions

### Give examples of 1D, 2D and 3D protein structure
- 1D -> Simple sequence / Secondary structure
- 2D -> Distance matrix of residues in the protein
- 3D -> Aminoacids plotted / Helices and beta strands may also be summarized visually

### Do you lose information when going from 3D to 2D?
- No, you can reconstruct 3D information
- You only lose the information if it is the protein or a mirrored version of the protein. But usually, one of the two versions occurs more frequently in nature, so you can guess, which version you have in front of you.

# Sequence Alignments 1

### Why compare 3D shapes, why not function?
- Shape determines function
- Sometimes similar structure implies similar function
- Shape is more easy to measure and compare than function
-> Predict function from shape

### What is a peptide?
Sequence of residues

### Can all proteins be made into a crystal?
No.

### Can we predict structure for all protein sequences?
No. For some, we can.

### Why would we want to predict secondary structure?
Strands and helices already tell us something about function.

### Name two ways to get to the shape of a protein
- By experiment (most accurate), for example X-ray crystallography
- Computational biology -> predict it from the sequence

### Why is it a bad idea to only match residues that are exactly the same?
- Some residues are more similar than others (two hydrophobic ones for example)
- Function might be thus more similar than when switching with a very different aminoacid
- Different residues can cause the same function

### What is homology?
Two genes / proteins have a common ancestor
-> differ in sequence, but often have similar structure and similar function
-> Homology is the existence of shared ancestry between a pair of structures

### How can you enforce a low number of connected blocks in a global alignment?
Instead of linear gap penalty, penalize gap opening and gap extension separately (typically gap opening = 10 * gap extension)

### How can you decide, which alignment is best?
- Ultimately, you can see if the structure is the same / the function is the same
- But more directly, you look at how many other proteins match with this alignment (GQ for example) and evaluate, how meaningful this alignment is -> again, signal values of proteins, which we know they have similar structure, vs background distribution in database

### How do you decide the word / seed size of BLAST?
- You try it out and then see if the BLAST scores are actually meaningful
- Run sequence against the entire database -> background distribution
- See if positive outliers (high scores / hits) exist

# Sequence Alignments 2

### How is a similar structure in 3D defined?
- < 0.2nm rmsd -> same
- > 0.5nm rmsd -> different

### Should you just run All vs All on PDB? What is the purpose of doing that?
- Purpose would be to find the different zones -> TP and FP depending on the alignment score -> find out what scores are meaningful
- Should be run on sequence-unique subset, not whole PDB
- But: not redundancy-reduced vs. redundancy-reduced, because there would be no similar pair left by definition!!

# Comparative Modeling

### What is the current state of the art of protein structure prediction?
- Works for some sequences
- No general prediction of 3D from sequence possible yet

### Where do the known protein structures come from?
- 90% of 120,000 from Xray
- 9% of 120,000 from NMR
- 1% of 120,000 from Electron Microscopy

### What is the big fight between X-ray dudes and NMR dudes?
X-ray dudes: you just can't measure it right
NMR dudes: what we show is motion and you guys don't see that with your method

### How does Cryo-EM work? What is the disadvantage?
- Take protein, freeze it, look at it under an EM
- Often, the resolution is 16-32 Angstrom -> is not the exact structure, only the rough shape

### Can two different proteins have the same surface?
Yes!

### How is secondary structure stabilized / determined?
With hydrogen bonds.

### What is a beta strand?
Two sequences of the same protein join (might be far away in sequence space) and stick together via the hydrogen bonds.

### What are two ways to annotate 1D secondary structure from 3D coordinates?
DEFINE: look at the shape and see if it looks like a helix
DSSP: look at the hydrogen bonding patterns (rules described by Pauling) and thus assign the likely secondary structure

### For how many sequences can you predict something about 3D structure? What can we predict for the rest?
- About half -> 55 million
- With comparative modeling
- For 55 million sequences, there is one region, where I can reliably predict something about 3D structure
- For the rest, we can predict 1D secondary structure

# Secondary Structure 1

### What is a difference between Helix and Sheet / Strand?
Helix is stabilized locally
Sheet is not

### Why would the same peptide sometimes be in a helix and sometimes in a strand?
If the binding partner for the strand is missing it might form a helix. Helix is stabilized locally, sheets are not.

### What is a family?
Proteins that have a similar structure
Can be defined by different threshold (think twilight zone)

### How can you measure the performance of secondary structure prediction?
- Q3 (three-state per-residue accuracy) -> simple match accuracy with 3 possible states
- Compare to baseline:
  - random guessing gets 33%
  - always guessing "other" gets 50% -> weight the three states differently to show that the 1st generation's 50% accuracy tell you more than the constant guessing!

### Why did people claim that 65% is the maximum for secondary structure prediction?
- Helix formation is local -> you see that in the windows
- Strand formation is not -> you don't have the necessary information
- The 65% number came from: people tried for many years all kinds of ideas and ML and they all hit against the 65% limit.
- So they thought 35% of secondary structure is determined by long range interactions

### What were problems of secondary structure prediction after the 2nd generation / before 1994?
- Hit against 65% mark -> must me max
- On beta-strands, the accuracy was only 40% -> slightly above random -> must be non-local
- Often short segments in predictions that contradict what we know -> you don't know how to use it For example, helix that consists of only 2 residues

### What would be shorter ways of encoding the network input than sparse coding / one-hot? What way performs best?
- 5 units -> binary coding of aminoacids
- 1 unit -> real value (simply the number)
- biophysical features
- old best: simple one-hot
- new best: one-hot PLUS biophysical features

### Why did sparse input encoding work better than the other simple encoding methods?
Because it makes no assumptions -> the others all introduce correlations that don't completely reflect reality -> the model first has to learn to untangle the correlations

### What is the difference between balanced and unbalanced training?
- Unbalanced directly gives the samples from the database -> more "other" training examples than helix and strand
- Balanced gives 3 examples (each from one class) at a time -> loss is summed
- Unbalanced scores 62% overall accuracy and scores "other" examples best
- Balanced scores 60% accuracy and predicts the three classes equally well -> 2% less, because a method that focuses on predicting the "other" well scores more
- Debunked the "beta strands are non-local => 40%" claim from the 2nd generation!! Because the balanced method does equally well on all three states -> 60% for every class -> no preference for one class on balanced data

### What is the whole process from sequence to 2ndary structure?
1. Sequence
2. Align it against database (BLAST)
3. Find the ones that belong to the same family
4. Extract alignment / profile
5. Put into one-level or two-level system (PHDsec)

### How can the prediction of a single network be improved?
- Jury decision -> differently trained networks
- As long as there is only white noise (-> errors that are not systematic), the performance improves

### Why does PROFsec still predict some proteins worse than random guessing?
- Pseudo-Science: strange features
- Actually: we don't know

# Secondary structure 2

### What else can you put in in addition to the profile?
- The current position
- How surprising is it that I have these residues in the aligned sequences at a specific position -> based on the biophysical features
























