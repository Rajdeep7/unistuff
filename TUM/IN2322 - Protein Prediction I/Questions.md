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

### Why is it a bad idea to only match residues that are exactly the same?
- Some residues are more similar than others (two hydrophobic ones for example)
- Function might be thus more similar than when switching with a very different aminoacid

### What is the difference between local and global alignment?
- Global -> Force the sequences to match end to end
- Local -> Find best local match (cut out the two matching subsequences)

### What is homology?
- Two genes / proteins have a common ancestor
- Might have similar function

### Why does brute force for aligning sequences globally not work? What is the DP solution for this?
- Have to select the gaps -> factorial down to gap number
DP:
- Write both sequences as row names and column names
- Write a 1 where two letters match, 0 otherwise
- Go from top left to (right / down / right and down) and sum up the values
- Optionally give a gap penalty for the right and down movement

### How can you enforce a low number of connected blocks in a global alignment?
- Instead of linear gap penalty, penalize gap opening and gap extension separately (typically gap opening = 10 * gap extension)

### What does the Needleman Wunsch algorithm do?
TODO

### What does the Smith Waterman algorithm do?
TODO

### How can you decide, which alignment is best?
- Ultimately, you can see if the structure is the same / the function is the same
- But more directly, you look at how many other proteins match with this alignment (GQ for example) and evaluate, how meaningful this alignment is

### What is a scoring matrix? Give an example and explain how it was created
- Gives the alignment score for two amino acids in a sequence alignment
- Example BLOSUM62
  - Took a bunch of proteins for which they knew that they had similar structure
  - Compute log odds (observed frequency of AB at same indey / expected frequency of AB at same index)
  - -> Aminoacid with high number on diagonal (W=17) almost never occurred instead of another aminoacid

### Why does the Blosum62 matrix have different values on the diagonal?
- Different values on diagonal, because some amino acids are more important to match than others
- Some diagonal values even lower than in non-diagonal cells, because the exact match for this AA is not as important as matching the two others

### What are issues with using DP for the alignments?
- Complexity is (length of protein)^2 -> No problem for two proteins, but a problem when you have to compare a protein to a whole databse
- How to choose parameters (gap penalty)?

### How can you speed up the alignments, when you have millions of proteins in the database and get thousands of queries per day?
- Small improvement: paralellization
- Big improvement: hashing / BLAST
  - Look for seeds of size 3 for example
  - Then only compare with sequences that also have these seeds
  
### How do you decide the seed size of BLAST?
- You try it out and then see if the BLAST matches actually also produce high alignment scores
- A seed size of 2 is mostly meaningless -> It is no better than just the scores when aligning random sequences with each other -> "background score distribution of the database"

### What does BLAST do?
TODO 

# 2
