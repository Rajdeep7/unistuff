### Fat and water loving and hating?
- Hydro
- Lipo
- Philic
- Phobic

### Central Dogma of Molecular Biology?
1. DNA Replication
2. Transcription to RNA
3. Transplation to Protein

### What is an ORF?
- Open Reading Frame
- DNA sequence that precisely codes for a protein
- DNA sequence consisting of start codon encoding M, intermediate codons, stop codons (not encoding aminoacids)
- In exercises we assume 1 ORF = 1 protein, but 1 to N is also possible

### Where do the 6 reading frames come from?
- 3 for different start positions
- 2 for complementary strand

### What is special for ORF for complementary strand?
- Read in reverse -> always from 5 to 3, but these numbers flip when taking the complement -> have to reverse reading
- ORF start > frame end

### What is the central file format? 
FASTA

### Name two databases for proteins
- UniProt / SwissProt for protein sequences
- PDB for protein structures

### Why do we want to align sequences?
- Make conclusions about structure and function
- Observe patterns of conservation
- Infer evolutionary relationships

### What does DP do?
- Divide a problem into consecutive subproblems
- Solution for each problem is based on its predecessors

### Name two alignment algorithms and their difference
- Needleman-Wunsch -> finds global alignment
- Smith-Waterman -> finds local alignment

### How does Needleman-Wunsch work?
1. Matrix with rows and colums = that of the two sequences  
2. Insert additional row and column at index 0 -> has a zero
3. Fill first row and column using gap penalty
3. Identity score matrix has zeros everywhere except for diagonal, and default gap penalty is -1
4. For each entry take the max of left + gp, upper + gp or left upper + score matrix
5. Go back from the bottom right cell using cells, whose numbers make sense
6. Save all possible paths to get all possible alignments!

### What are the limitations of global alignment?
1. Can't detect local regions of high similarity
3. Can't align a fragment and a sequence

### How does Smith Waterman work?
- Matrix cell values are always >= 0 -> Fill first row and column with zeros
- Start traceback at the cell with max value and go back to cell with 0 value
- Finds optimal local alignment

### Our algos only do pairwise alignment. How can we do multiple alignments?
- Combine pairwise alignment (tree or consecutive ...)
- Search strategies needed to avoid combinatorial explosion

### What do we need for constructing a PSSM?
1. Information about substitutions occuring in the protein -> MSA
2. Differentiation between favored and unfavored substitutions. Define:
   - favored = more often than expected
   - unfavored = less often than expected
   - expected = either 0.05 or actual background distribution
3. Transformation into positive and negative scores

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
1. Help improve alignments (local and global) -> Instead of BLOSUM62. You can even align two PSSMs
2. Condense information about the evolution of a protein
   - Conserved positions are easy spot
   - Important input feature for many prediction methods
3. Help to find protein homologs in databases

### What is BLAST?
- Searches database for similar sequences
- Uses seeds for hit determination
- The hits are scored by expanding the matching seeds with local alignment
- Seed = short sequence (3-gram) that has a high pairwise score to the query sequence  
  -> Go through 20 x 20 x 20 seeds and find the seeds that score highest when moved over the sequence
- Database stores, which proteins contain which seeds. Seeds are not matched against the sequence, the sequence needs to contain exactly the seeds!
- Does not specify what to do with the regions that are not covered by the local alignments
- Can also do Seed vs PSSM (use row index as sequence position)

### What is PSI-BLAST?
Iterative BLAST
1. Use BLOSUM62 scores for first search against database
2. Build PSSM based on high-scoring hits
3. Search again using the PSSM
4. Repeat 2

### What is a problem of PSI-BLAST?
False hits can pollute the PSSM

### What is an advantage of PSI-BLAST?
Can find more distantly related protein sequences.

### What numerical types are there?
- integer
- interval-scaled (°C)
- ratio-scaled (0 means absence, e.g. kg or meters)

### What is the machine learning workflow?
1. Preprocessing
2. Data Analysis
3. Training the Network
4. Performance Evaluation
