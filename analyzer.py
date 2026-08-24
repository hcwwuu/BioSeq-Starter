def validate_sequence(seq): #无对应函数
    if not seq:
        return False
    
    valid_bases = {"A", "T", "C", "G"}
    for base in seq:
        if base not in valid_bases:
            return False
    return True

def count_bases(seq):#sequence.count("A")
    #建立一个字典
    counts = {
        "A": 0,
        "T": 0,
        "C": 0,
        "G": 0
    }
    for base in seq:
        counts[base] += 1
    return counts

def gc_content(seq):#gc_fraction(sequence)
    counts = count_bases(seq)
    gc_count = counts["G"] + counts["C"]
    return gc_count / len(seq)

def reverse_complement(seq):#sequence.reverse_complement()
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    result = ""
    for base in reversed(seq):#reversed()函数返回的是反向的下标（迭代器）
        result += complement[base]
    return result