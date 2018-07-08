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
- "A protein domain is a part of a given protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain."
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

### Why do we do alignments?
- To find out, how similar two proteins are in sequence comparison
- Similar sequences tend to have similar shapes

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
- -> Homology is the existence of shared ancestry between a pair of structures

### How does brute force work for global alignments?
- The hardcore brute force would be to go through all possible combinations -> combinatorial explosion
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
  - sequence - sequence
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

### Should you just run All vs All on PDB? What is the purpose of doing that?
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
- Given that we have a multiple sequence alignment, compute the score for each residue at each position
- -> Specific to a protein family

### What is PSI-Blast?
- Position-Specific Iterative Basic Local Alignment Tool
- Steps:
  1. Fast hashing (BLAST) -> Query database with sequence and substitution metric (BLOSUM)
  2. Dynamic programming extension between matches (Smith-Waterman)
  3. Compile statistics -> Find the scores that are meaningful
  4. Collect all pairs and build profile
  5. Iterate (find new matches using new profile) -> Query database with profile
- Output is a Profile -> used today to generate profiles
  
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
  - Search database for loop sequence and infer its structure

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

### How can you measure comparative modeling performance?
- CASP Challenge
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
- From diffraction patterns to result: days
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
- Better solution, if we already have aligned some proteins and they belong to the same family: 
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

### What is the second generation 2nd structure prediction method?
- Also look at the window (segment) instead of just at one aminoacid
- Pad start and end with additional 21st padding-aminoacid
- TODO: How the counting works

### Why did people claim that 65% is the maximum for secondary structure prediction?
- Helix formation is local -> you see that in the windows
- Strand formation is not -> you don't have the necessary information
- The 65% number came from: people tried for many years all kinds of ideas and ML and they all hit against the 65% limit.
- So they thought 35% of secondary structure is determined by long range interactions

### What were problems of secondary structure prediction after the 2nd generation / before 1994?
- Hit against 65% mark -> must me max
- On beta-strands, the accuracy was only 40% -> slightly above random -> must be non-local
- Often short segments in predictions that contradict what we know -> you don't know how to use it
  For example, helix that consists of only 2 residues

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
- Adds a structure to structure network
- 2nd level network that has output of previous network -> per position 3 inputs + padding input
- 2nd level has 17 positions as input
- 2nd level is trained after 1st level
- 2nd level network (hopefully) learns things like HLHL doesn't exist or helices have at leask k length -> better segment prediction
- still only 60% accuracy

### What is a spacer unit?
Padding input unit

### How can you get more data than PHDsec as input?
- Use evolutionary information
- Evolution tells you what works -> only the changes that work are observed
- Evolutionary profile captures history of an individual protein  
  -> tells us how important what aminoacid at which position is
  -> the residues that are the same across the family for a specific position are not chosen randomly. they might seem randomly distributed in 1D but in 3D they often act / stick together
  -> on the one hand, often 63% of the residues of a protein can be changed to another aminoacid, but if you change 5 at random you will very likely change the structure!
- Instead of one-hot encoding, feed the log probability vector from the profile as input -> # inputs per position = 21 remains the same!
- Predicted probability also strongly correlates with actual accuracy!

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
- Very strange features (the prevention of freezing protein for example)
- No / low profile
- But: not scientific, because we also would have to check that other proteins with strange features / low profile perform that bad!
- we don#t know 
 
# Secondary structure 2

### What else can you put in in addition to the profile?
- The current position
- How surprising is it that I have these residues in the aligned sequences at a specific position -> based on the biophysical features

### What needs to be satisfied to say method A is better than method B?
- Measure needs to be higher
- Use the same measure
- Use the same dataset
- Careful with train test split!! There must not be highly similar proteins pairs with one in the train and one in the test split, where comparative modeling would work! 
- Std error intervals don't overlap
- Is one of them older and 
  - there is new data available?
  - was found to have made a mistake?
  
### What is a pre-release test?
Use data added after both methods had been developed

### What types of significance are there?
- Scientific significance -> Scientific expert evaluates how meaningful the score difference is based on experience
- Statistical significance 
  -> standard error (= sigma / sqrt(proteins))
  -> age doesn't matter, only the numbers!
  
### You try out a hyperparameter that performed worse in validation and it turned out to perform better on the test set. What do you do?
- If you trust your process, your validation set is the best way to pick the hyperparameter, so you reporting the test error was the right method. It is then likely that the difference is not significant or something is flawed between the val and test set.
- Never use the test set for any decision!! Only to report the number

# Transmembrane Helix Prediction
- There is more than one membrane for eukaryotes! -> inner membrane and outer membrane

### How many percent of the known structures are transmembrane helix proteins? How many of the total proteins out there?
- Less than 2% of known (only counting unique, then WAY less)
- About 20% in total!

### Why is a membrane important?
- Keep malicious things away and keep important things inside
- Garbage disposal
- Communication with the environment

### What is the lipid bilayer?
- Makes up the cell membrane and also the cell nucleus membrane
- Separates inside and outside
- Keeps proteins where they should be
- Hydrophobic inside, hydrophobic outside 
- Hydrophobic is sticky!
- When protein goes through membrane, its environment is suddenly no more water but hydrophobic!
- Easy to pull protein horizontally but hard to get it through the membrane

### Why do most drugs targets tend to be found in membranes or are extra-cellular?
- Because its the easiest point to get to
- As soon as you get through the membrane, other processes kick in, which you also have to target

### Why are so little membrane proteins modelled?
- It is very hard to measure them
- They form at the membrane -> when you get them out of the membrane they fall apart

### What are interesting features of membrane proteins?
- Number of transmembrane helices
- Topology -> Orientation

### Why does membrane protein prediction go wrong? What is the solution?
- Because membrane proteins have a different composation than non-membrane proteins
- Membrane proteins have hydrophobic residues on outside AND inside!
- Solution: just focus on hydrophobic residues and see, how they form structure
- Problem: how do you define hydrophobicity? -> multiple scales available!

### What is the solution for using the standard protein prediction method on membrane proteins?
- Find hydrophobic residues in the protein and only based on that predict the (number of) transmembrane helices
- Problem: two thresholds:
  - Higher one says ok if it is that hydrophobic, it is a transmembrane helix
  - Lower one says ok if it is only that hydrophobic but is more than 20 residues long, it is a transmembrane helix
- Refine thresholds (and also pick the hydrophobicity scale) by trying it out -> Predict transmembrane helices for the few membranes, for which we know the structure, and see how correct the predictions are
- How do you define a correct prediction? How do you tune the threshold parameters and the choice of hydrophobicity scale?
  - Predict the right number of transmembrane helices
  - How many membrane helices there are is likely more important than predicting them exactly!

- Define a hydrophobicity index such that you can optimally predict membrane helices (2001 approach) rather than just choosing the known structures to predict the thresholds for hydrophobicity, you choose the hydrophobicity index -> almost like the propensity
- You train the network only on membrane helices or on (proteins with membrane helices and non-membrane helices)
- You don't have HEL anymore as output, you have membrane / not membrane as binary output

### Why does the second level now work too well? Solution?
- It predicts too long helices than ground truth (usually twice as long)
- Solution: DP!
- Membrane helices have between 15 and 25 helices
- Create a pool of all segments between 15 and 25 that look like transmembrane helices
- For each of these, compute the average T probability
- For mu = 1 to N_pool:
  - Take the one with the highest average T probability
  - Take the k-1 next highest that are not conflicting with the ones found (that is not overlapping with the ones already found)
- You need a stop criterion for adding helices -> for example, when you add one with average probability < 0.5
- Then you compute the positive inside stuff and get the orientation

### What is the positive inside rule? How does it help?
- For transmembrane proteins there are more positively charged residues in parts that go inside the cell (intra-cytoplasmic)
- You can use this to predict the orientation of the transmembrane helix

### What is a hydrophobicity scale?
- Gives each aminoacid a hydrophobicity value

### How can you decide which hydrophobicity scale is the best?
- Predict helices with them 

### What is a transmembrane helix?
- Helix that goes through the membrane, usually more than about 20 residues long

# Intrinsically Disordered Proteins

### What are Natively / Intrinsically Disordered / Unstructured Proteins?
- Unbound, the protein is wobbling (not a fixed structure) -> if you take two photos of it you won't see the same structure
- Upon binding, the protein adopts a fixed structure -> if you take two photos of it it will always be the same structure
- Can "unlock" different locks -> Adopts to different proteins with a different structure

### What is the fly casting analogy?
- IDP is a line wobbling around -> like a fly at the end of a string
- Upon contact with its target, a weak contact is established, which pulls the rest in
- Then the IDP folds around the target upon approach
- -> increases reach of protein
- -> can bind to different target proteins

### What is NORS?
- No regular secondary structure
- Defined as less than 5% helix or strand in over 70 residues

### What are the types of NORS?
- Connecting loops
- Floppy ends
- Wrapping loops 
- Floppy domains

### What is "loopy" disorder?
- Many proteins have long regions where we see no regular secondary structure (Helix or Strands)

### Where would you put the b-value threshold?
- You measure proteins and take a look at where they move how much -> gives you the b-value
- Then you want binary classifcation (flexible or not flexible) -> need b-value threshold
- Don't put the threshold at the peak, because every experiment makes some error -> if you put the threshold at the peak, the tiniest mistake has the strongest possible effect. That makes it the hardest for the ML device to learn.
- You can also not put the threshold at an extreme value, because then you don't have enough points left from the one class (unbalanced data!)
- Therefore, the solution lies somewhere in the middle

### How can you predict residue flexibility?
- PROFbval
- Solve the threshold problem for the b-values
- Then use the same 1st level network from secondary structure prediction with profile as input

### What are two methods of predicting NORS?
- Predict b-values / flexibility.
  - needs experimental data (but not experimental disorder data, only dynamics. that we can measure (NMR))
  - Caution: protein dynamic doesn't directly imply protein disorder!
- Predict short NORS regions / distinguish unstructured from well-structured loops

### Method 2
- Simply predict secondary structure 
- Then define NORS as less than 5% regular structure in over 70 residues
- Problem: We also want to find NORS in peptides of like 30 residues. By definition, we cannot do that in this way. Making the 70 to 30 -> the method finds a lot of false positives (positive being NORS)
- Solution: positive = all regions with < 5% in > 70, negative = whole PDB
- Problems:
  - the set of positives does not contain a single example of what we want to learn (we want to learn 30 residues loops that are disordered)
  - false negatives. there is a lot of regions in the proteins in the PDB that is actually disordered. this could break the ML system
- Solution: only the signal is consistent!

### Method 3
- IUPred
- Ucon: unstructured regions from contact prediction
- Predict contact-deprived regions
- Because on contact, they bind and cannot move anymore -> predict contact to predict movement
- If subsequent residues are unlikely to form a contact, this might be a NORS

There is no experiment that clearly shows disorder
-> We cannot measure disorder. What we can measure is what we cannot see
-> Dunker-Hypothesis: Residues not visible in 3D structures share disorder

Disorder is more difficult to conserve (in an evolutionary sense) than regular secondary structure. Disorder is more sensitive to random changes!

### What is a dark proteome?
Part in a protein where you know nothing about the 3D structure
- No comparative modeling possible
- No experimental structure
- 15% dark proteins for Eukaryotes. Dark protein -> all dark
- Why are these proteins dark? Some are disordered, some are ordered, for many we cannot explain why they are dark

### What is a proteome?
The proteome is the entire set of proteins that is, or can be, expressed by a genome, cell, tissue, or organism at a certain time.

