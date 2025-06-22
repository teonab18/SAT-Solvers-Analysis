def solve(clauses):
    if any(len(c) == 0 for c in clauses):
        return None 

    if not clauses:
        return {}
    literal = next(iter(clauses[0]))
    variable = literal.replace('neg', '')
    solution = solve(simplify(clauses, variable))
    if solution is not None:
        solution[variable] = True
        return solution
    solution = solve(simplify(clauses, f"neg{variable}"))
    if solution is not None:
        solution[variable] = False
        return solution
    
    return None 
def simplify(clauses, unit_literal):
    new_clauses = []
    complement = f"neg{unit_literal}" if not unit_literal.startswith('neg') else unit_literal[3:]
    for c in clauses:
        if unit_literal in c:
            continue 
        if complement in c:
            new_clauses.append(c - {complement})
        else:
            new_clauses.append(c)
    return new_clauses

def dpll(clauses):
    solution = solve(clauses)
    return solution is not None