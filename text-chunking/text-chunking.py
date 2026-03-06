def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    result=[]
    step_size=chunk_size-overlap
    n=len(tokens)
    if n==0:
        return result
    if n<chunk_size:
        return [tokens]
    for i in range(0,n,step_size):
        if i+chunk_size>n:
            break
        result.append(tokens[i:i+chunk_size])
    return result