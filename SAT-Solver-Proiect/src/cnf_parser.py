def parse_cnf(filepath):

    clauses = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('c') or line.startswith('p') or line.startswith('%'):
                    continue
                literals_str = line.split()
                if literals_str and literals_str[-1] == '0':
                    literals_str = literals_str[:-1]
                
                if not literals_str:
                    continue
                clause = set()
                for lit_str in literals_str:
                    num = int(lit_str)
                    if num > 0:
                        clause.add(str(num)) 
                    else:
                        clause.add('neg' + str(abs(num))) 
                
                clauses.append(frozenset(clause))
                
    except FileNotFoundError:
        print(f"EROARE: Fișierul {filepath} nu a fost găsit.")
        return None
    except Exception as e:
        print(f"EROARE la parsarea fișierului {filepath}: {e}")
        return None
        
    return clauses