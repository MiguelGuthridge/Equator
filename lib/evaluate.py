from . import parse
from . import segment

def evaluate(inp: str):
    # Parse input
    prep = parse.prepString(inp)
    
    # For each expression, create a segment for it
    solutions = []
    for p in prep:
        seg = segment.Segment(p)
        solutions.append(str(seg.evaluate()).replace("**", "^"))

    return solutions