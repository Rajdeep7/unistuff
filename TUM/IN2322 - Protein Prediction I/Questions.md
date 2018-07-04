# Introduction

### How do you get from DNA to a protein?
- DNA -> RNA -> Protein
- DNA and RNA have 4 letter alphabet of nucleotides
- Protein has 20 letter alphabet (aminoacids) 
- Codon of 3 nudleotides (1 codon = 1 triplet) for one amino acid

### What is the difference between eukaryotes and prokaryotes?
- Eukaryotes have a nucleus

### How many different proteins are in a human? How many proteins are known in total?
- Around 20K in a human, 110M known in total

### What does secondary structure refer to?
- Denotes if the aminoacid is in a Helix or beta strand
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
- Area in the DNA that is used for building the protein (in between the start and the end block)

### What is a domain?
- Region in the protein denoting the evolutional context of the protein (?)
- Subsequence in the protein sequence 
- -> many different proteins have that or a similar subsequence -> maybe is a domain

### How many proteins have a single domain?
- Less than 30%

### Why would evolution "decide" to merge two protein (domains)?
- Because Protein A and B have to act together -> have to bind locally together 
- By constructing C = A + B, the proteins don't need to meet anymore
- -> Join these sequences in the genome to save time

### What does the multiple sequence alignment do?
- Has as input many different proteins and aligns them in a way that their domains / subsequents match
- Problem: similar but different sequences may belong to the same domain

### Why do we compare the sequences instead of 3D structure?
- For most proteins, we don't have the 3D structure
- Also, comparing sequences is easier 

### What is the tradeoff between global and local comparison?
- Deranged red man -> has the same parts but doesn't match globally at all
- -> matches locally, but problem is, where to stop. You can always go onto a lower level of comparison, where a lot matches (bag of words, for example).
- Between domains, you will see subsequences that are similar -> why not just make that into a valid domain?
- What is a valid unit for comparison?
- Answer: test if the functionality is also the same given that the alignment says that they are similar
- -> has to differ significantly from background distribution

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





