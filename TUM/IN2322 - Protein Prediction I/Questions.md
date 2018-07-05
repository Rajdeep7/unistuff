# Introduction

### How do you get from DNA to a protein?
- DNA -> RNA -> Protein
- DNA and RNA have 4 letter alphabet of nucleotides
- Protein has 20 letter alphabet (aminoacids) 
- Codon of 3 nudleotides (1 codon = 1 triplet) for one amino acid

### What is the difference between eukaryotes and prokaryotes?
- Eukaryotes have a nucleus

### How many different proteins are in a human? 
Around 20K in a human

### How many proteins are known in total?
110M known in total

### How many protein structures are known?
120,000

### What is the length of the shortest and the longest protein?
From 35 to 35K residues

### What does secondary structure refer to?
- Denotes if the aminoacid is in a Helix or beta strand etc.
- Is 1D information -> each aminoacid gets a value

### What are the two parts that make up an amino acid?
- Side-chain (different for each amino acid)
- Backbone (same for all amino acids) -> Contains C-alpha

### How can amino acids be joined into a chain?
- Called dipeptide for 2
- Backbones are connected (one amino acid is flipped vertically)

### What are some properties of amino acids?
- Positively charged (2)
- Negatively charged (2)
- Hydrophobic -> Since protein folds in water, these will likely be inside of the protein
- Hydrophilic -> Since protein folds in water, these will likely be at the border of the protein
- Polar (5)

### What is an intron?
- A region in the DNA that is cut out -> not used to build proteins

### What is an exon?
- Area in the DNA that is used for building the protein (between the start and the end block)

### What is a domain?
- Region in the protein denoting the evolutional context of the protein (?)
- Subsequence in the protein sequence 
- -> many different proteins have that or a similar subsequence -> maybe is a domain
- folds independently of other sequences in the protein

### How many proteins have a single domain?
- Less than 30%

### Why would evolution "decide" to merge two protein (domains)?
- Because Protein A and B have to act together -> have to bind locally together 
- By constructing C = A + B, the proteins don't need to meet anymore
- -> Join these sequences in the genome to save time

### What does the multiple sequence alignment do?
- Has as input many different proteins and aligns them in a way that their domains / subsequences match
- Problem: similar but different sequences may belong to the same domain

### Why do we compare the sequences instead of 3D structure?
- For most proteins, we don't have the 3D structure (Only for 120K proteins)
- Also, comparing sequences is easier 
- 3D structure comparison would be better, because the structure does not have to be similar for similar sequences

### What is the tradeoff between global and local comparison?
- Deranged red man -> has the same parts but doesn't match globally at all
- -> matches locally, but problem is, where to stop. You can always go onto a lower level of comparison, where a lot matches (bag of words, for example).
- Between different domains, you will see subsequences that are similar -> why not just make that into a valid domain?
- What is a valid unit for comparison?
- Answer: score has to differ significantly from background distribution for proteins where you know that they are functionally or structurally similar (from one family)

### How can we compare 3D shapes?
With 2D matrix comparison
1. Find the best global superposition (points, where both shapes are the closest)
2. Compute for each shape the distance matrix between its points (isolated from the other shape)
3. Compare both matrices -> RMSD (can also compare subregions of the matrix)

### What is a residue?
An aminoacid in a protein

### Give examples of 1D, 2D and 3D protein structure
- 1D -> Simple sequence / Secondary structure
- 2D -> Distance matrix of residues in the protein
- 3D -> Aminoacids plotted / Helices and beta strands may also be summarized visually

### Do you lose information when going from 3D to 2D?
- No, you can reconstruct 3D information
- You only lose the information if it is the protein or a mirrored version of the protein. But usually, one of the two versions occurs more frequently in nature, so you can guess, which version you have in front of you.

# Sequence Alignments 1
-> You find a new protein in a new disease and you want to know what it does
-> Alignments answer the question "how similar are proteins?"

### Why compare 3D shapes, why not function?
- Shape determines function
- Sometimes similar structure implies similar function
- Shape is more easy to measure and compare than function
- -> Predict function from shape

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

### What is the difference between local and global alignment?
- Global 
  -> Forced to compare the sequences from end to end
  -> Assumes that both sequences have a single domain
  -> Every residue of the subsequence has to be matched to something
- Local 
  -> Find best local match (cut out the two matching subsequences)
  -> Allows ignoring subsequences that would decrease the alignment score
  -> Good for matching proteins with multiple domains

### What is homology?
- Two genes / proteins have a common ancestor
- -> differ in sequence, but often have similar structure and similar function

### How does brute force work for global alignments?
- Needleman Wunsch
- Dynamic programming
- Write both sequences as row names and column names
- Write a 1 where two letters match, 0 otherwise
- Go from top left to (right / down / right and down) and sum up the values
- Optionally allow gaps in between the proteins and not just at start and end
- Optionally give a gap penalty for the right and down movement

### How can you enforce a low number of connected blocks in a global alignment?
- Instead of linear gap penalty, penalize gap opening and gap extension separately (typically gap opening = 10 * gap extension)

### What does the Needleman Wunsch algorithm do?
- Dynamic programming
- Global alignments
- Write both sequences as row names and column names
- Write a 1 where two letters match, 0 otherwise
- Go from top left to (right / down / right and down) and sum up the values
- Optionally allow gaps in between the proteins and not just at start and end
- Optionally give a gap penalty for the right and down movement

### What does the Smith Waterman algorithm do?
- Local alignments 

### How can you decide, which alignment is best?
- Ultimately, you can see if the structure is the same / the function is the same
- But more directly, you look at how many other proteins match with this alignment (GQ for example) and evaluate, how meaningful this alignment is -> again, signal values of proteins, which we know they have similar structure, vs background distribution in database

### What is a scoring matrix? Give an example and explain how it was created
- Gives the alignment score for two amino acids in a sequence alignment
- Example BLOSUM62
  - Took a bunch of proteins for which they knew that they had similar structure
  - Go through all pairs of proteins
  - Compute log odds (observed frequency of AB at same index / expected frequency of AB at same index = M / p)
  - -> Aminoacid with high number on diagonal (W=17) almost never occurred instead of another aminoacid

### Why does the Blosum62 matrix have different values on the diagonal?
- Different values on diagonal, because some amino acids are more important to match than others
- Some diagonal values even lower than in non-diagonal cells, because the exact match for this AA is not as important as matching the two others

### What are issues with using DP for the alignments?
- Complexity is in the order of (sequence length)^2 -> No problem for two proteins, but a problem when you have to compare a protein to a whole databse
- Per year, x 2 entries in database and x 20 needed comparisons
- How to choose parameters (gap penalty)?

### How can you speed up the alignments, when you have millions of proteins in the database and get thousands of queries per day?
- Small improvement: paralellization
- Big improvement: hashing / BLAST
  1. Don't align the entire sequence, but only small words that match exactly
  2. Extend the matches locally -> few much smaller subproblems than one big problem on full sequence
  3. Ignore the gaps between the extended matches
  4. Use BLOSUM or other matrix for scoring
  
### How do you decide the word / seed size of BLAST?
- You try it out and then see if the BLAST scores are actually meaningful
- Run sequence against the entire database -> background distribution
- See if positive outliers (high scores / hits) exist

# Sequence Alignments 2

### What are the different zones?
- Do all vs all comparison of sequences and structure in PDB
- Scale from 0 to 100% sequence identity
- TP -> pairs of proteins with similar structure
- FP -> pairs of proteins with different structure
- Daylight Zone (40 to 100)
  - sequence similar => structure similar
  - TP > FP
  - sequence sequence
- Twilight Zone (20 to 40)
  - sequence not so similar, structure sometimes similar
  - TP increase, FP explode
  - sequence - profile
- Midnight Zone 
  - No significant prediction ability
  - FP >> TP
  - profile - profile

### How is a similar structure in 3D defined?
- < 0.2nm rmsd -> same
- > 0.5nm rmsd -> different

### Should you just run All vs All on PDB? What is the purpose of doing that
- Purpose would be to find the different zones -> TP and FP depending on the alignment score -> find out what scores are meaningful
- Should be run on sequence-unique subset, not whole PDB
- But: not redundancy-reduced vs. redundancy-reduced, because there would be no similar pair left by definition!!

### Why can't you do simply DP for multiple alignments?
- NP complete, for 3 sequences it is already O(N1 x N2 x N3)
- Hack 1: do only pairwise comparisons
- Hack 2: use a tree -> join two and then run alignment on joined version
- When joining two residues and they differ, take the most likely residue according to the blosum matrix

### What is a PSSM?
- Position specific scoring matrix
- Given that we have an multiple sequence alignment, compute the score for each residue at each position
- -> Specific to a protein family

### What are the steps in computing the PSSM?
TODO

### What is PSI-Blast?
- Position-Specific Iterative Basic Local Alignment Tool
- Steps:
  1. Fast hashing (BLAST) -> Query database with sequence and substitution metric (BLOSUM)
  2. Dynamic programming extension between matches (Smith-Waterman)
  3. Compile statistics -> Find the scores that are meaningful
  4. Collect all pairs and build profile
  5. Iterate (find new matches using new profile) -> Query database with profile
  
# Comparative Modeling

### What is comparative modeling?
- Background: similar sequences have similar structure
- (Nobel prize for: same sequence always folds into the same structure)
- Want to predict structure for target protein
- Steps:
  1. Identify template / database search (BLAST / PSI-BLAST etc.)
  2. Align target and template (DP, profile-profile)
  3. Build model
     - simplest model: just take template's coordinates and insert the target's residues
     - problem with simplest model: 
       - if the other one has one residue inserted it completely destroys the rest of the fitting (however, that is usually covered by the alignment!!)
       - if the alignment was wrong, it breaks
       - might not correspond to the actual secondary structure
  4. Assess model
  5. Refine
  
### What are typical comparative modeling errors?
- Mis-alignment -> breaks
- Template was wrong

### What are loops? Solution?
- Target sequence has additional residues inserted in comparison with template
- -> you have two anchor points, between that you have no idea how the structure looks like
- Solutions: 
  - Molecular simulation
  - Search database for loop sequence

### Name two methods for comparative modeling
- MODELLER
- SWISS-MODEL
  
### What does MODELLER do?
- Comparative modeling -> very accurate
- Find template with BLAST / PSI-BLAST
- Align target and template (DP, profile-profile, etc.)
- Build model -> deal with loops that are missing in template etc.
- Assess model
- Refine
  
### What does SWISS-MODEL do?
- Comparative modeling for non-experts
- Find template with BLAST / PSI-BLAST
- Copy co-ordinates

### What is CASP?
- Critical Assessment of Structure Prediction
- Challenge, where not even the Organizers know the test targets (structures)
- Participants give their predictions

### What is the current state of the art of protein structure prediction?
- Works for some sequences
- Only homology modeling good
- No general prediction of 3D from sequence possible yet

### Where do the known protein structures come from?
- 90% of 120,000 from Xray
- 9% of 120,000 from NMR
- 1% of 120,000 from Electron Microscopy

### What are the steps of X-ray crystallography?
1. Crystallize
2. Diffraction pattern with x-rays
3. Electron density map
4. Fit atomic model
5. Refine step 2 and iterate

### How long takes X-ray crystallography?
- From diffraction to result: days
- Getting the diffraction pattern: more than a year

### How does NMR work?
- Nuclear Magnetic Resonance
- Take protein from its environment, put it in tube, put the tube under a magnet
- Does not modify the protein!
- Measurements only give constraints -> Models have to be fitted -> Several models as output that are compatible with the data 
- -> is uncertain -> might be due to dynamic regions of the protein (b factors)
- X-ray dudes say: you just can't measure it right. NMR dudes say: what we show is motion and you guys don't see that with your method
- Even the fitting after you have the experimental data takes months
- Limitation: because NMR cannot distinguish between "was it the aminoacid at position 5 or 15", it becomes impossible to to NMR with proteins of length > 200 and most human proteins have such a long length.

### How does Cryo-EM work? What is the disadvantage?
- Take protein, freeze it, look at it under an EM
- What is the disadvantage? Often, the resolution is 16-32 Angstrom -> is not the exact structure, only the rough shape

### Can two different proteins have the same surface?
Yes!

### How is secondary structure stabilized / determined?
With hydrogen bonds.

### What is a beta strand?
Two sequences of the same protein join (might be far away in sequence space) and stick together via the hydrogen bonds.

### What are two ways to annotate 1D secondary structure from 3D coordinates?
- DEFINE: look at the shape and see if it looks like a helix
- DSSP: look at the hydrogen bonding patterns (rules described by Pauling) and thus assign the likely secondary structure

### In comparative modeling, what is the difference between target and template?
- Target: protein to model (predict)
- Template: protein to model from

### For how many sequences can you predict something about 3D structure? What can we predict for the rest?
- About half -> 55 million
- With comparative modeling
- For 55 million sequences, there is one **region**, where I can reliably predict something about 3D structure
- For the rest, we can predict 1D secondary structure

# Secondary Structure 1

### What are the states of secondary structure?
DSSP secondary assignment has 8 states:
1. H = Helix
2. E = Extended (strand)
3. B = Beta-bridge
4. T = Turn
5. S = Bent
6. " " = Loop

Or you just say helix, strand (E and B) and other.

### What is a difference between Helix and Sheet / Strand?
- Helix is stabilized locally
- Sheet is not

### Why would the same peptide sometimes be in a helix and sometimes in a strand?
If the binding partner for the strand is missing it might form a helix. Helix is stabilized locally, sheets are not.

### What is a profile?
- When aligning proteins, the simplest method is to align identity
- But: you want to consider biophysical features
- Solution: generic exchange matrix, such as Blosum
- Better solution if we already have aligned some proteins and they belong to the same family: 
  - Look at a particular position and look at the distribution of residues at that position
  - -> "At position X, there is a Alanine that you cannot change!!! But you are free to do so at position Y"
  
### What is a family?
- Everything that has a similar structure
- Can be defined by different threshold (think twilight zone)
  
### What is the first generation / simplest 2nd structure prediction method? When? How good?
- Proline breaks a helix!
- Take all proteins with known structure and convert them to 1D with DSSP
- Count the 2nd structure states for each amino-acid for each protein and build probability distribution for each amino-acid
- Assign single 2nd structure label to each amino-acid (simply take the most frequent one)
- From 1957 to 1970s
- Around 50% accuracy (but always guessing other also gets 50%)

### How can you measure the performance of secondary structure prediction?
- Q3 (three-state per-residue accuracy) -> simple match accuracy with 3 possible states
- Compare to baseline: 
  - random guessing gets 33%
  - always guessing "other" gets 50% -> weight the three states differently to show that the 1st generation's 50% accuracy tell you more than the constant guessing!

### What is DSSP?
- Converts 3D structure to secondary structure
TODO

### What is the second generation 2nd structure prediction method?
- Also look at the window (segment) instead of just at one aminoacid
- Pad start and end with additional 21st padding-aminoacid
- TODO: How the counting works

### Why did people claim that 65% is the maximum for secondary structure prediction?
- Helix formation is local -> you see that in the windows
- Strand formation is not -> you don't have the necessary information
- 35% of secondary structure is determined by long range interactions
- The 65% number came from: people tried for many years all kinds of ideas and ML and they all hit against the 65% limit.

### What were problems of secondary structure prediction after the 2nd generation / before 1994?
- Hit against 65% mark -> must me max
- On beta-strands, the accuracy was only 40% -> slightly above random -> must be non-local
- Often short segments in predictions that contradict what we know -> you don't know how to use it

### What would be shorter ways of encoding the network input than sparse coding / one-hot? What way performs best?
- 5 units -> binary coding of aminoacids
- 1 unit -> real value (simply the number)
- biophysical features
- old best: simple one-hot
- new best: one-hot PLUS biophysical features

### Why did sparse input encoding work better than the other simple encoding methods?
Because it makes no assumptions 
-> the others all introduce correlations that don't completely reflect reality
-> the model first has to learn to untangle the correlations

### What is the difference between balanced and unbalanced training?
- Unbalanced directly gives the samples from the database -> more "other" training examples than helix and strand
- Balanced gives 3 examples (each from one class) at a time -> loss is summed
- Unbalanced scores 62% overall accuracy and scores "other" examples best
- Balanced scores 60% accuracy and predicts the three classes equally well -> 2% less, because a method that focuses on predicting the "other" well scores more
- Debunked the "beta strands are non-local => 40%" claim from the 2nd generation!! Because the balanced method does equally well on all three states -> 60% for every class -> no preference for one class on balanced data

### What is PHDsec?
- structure to structure network
- 2nd level network that has output of previous network -> per position 3 inputs + padding input
- 2nd level has 17 positions as input
- 2nd level is trained after 1st level
- 2nd level network (hopefully) learns things like HLHL doesn't exist or helices have at leask k length -> better segment prediction
- still only 60% accuracy

### What is a spacer unit?
Padding input unit

### How can you get more data than PHDsec as input?
- Use evolutionary information, for example 
- TODO



