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
  6. Problem: What to do with gaps in the alignment?

### When can comparative modeling go wrong?
- When you don't find a template
- When the template is a false positive (likely if too much in the twilight zone)
- When there are gaps in the alignment, but there are solutions to this
- Mis-alignment breaks the prediction

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

### How can you find out that you picked the wrong comparative modeling template?
You have a lot of clashes.

### What is disorder?
- Usually, proteins have a unique 3D structure in water, otherwise they would not be able to function correctly
- Disorder = at least a part of the protein is not adopting a unique 3D structure 
- -> When looking at it at two different times, it does not have the same structure
- What the protein will look like is still written 100% in the sequence. It is just that what stands there is not "form a helix or strand" but now the information is "have a region that is disordered"
- Upon binding, it adopts structure -> orders upon binding
- Adopts to different locks with different structure
- Flexibility and dynamics enable its function

### Explain simple methods (1st generation, 2nd generation, 3rd generation methods) for secondary structure prediction
















