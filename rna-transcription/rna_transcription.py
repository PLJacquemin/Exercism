corr_bases = {"A":"U","C":"G","T":"A","G":"C"}

def to_rna(dna_strand):
    return "".join([corr_bases[base] for base in dna_strand])
