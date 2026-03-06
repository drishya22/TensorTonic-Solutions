def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    freq=dict()
    total=dict()
    n=len(targets)
    for i in range(n):
        if categories[i] in total:
            total[categories[i]]+=targets[i]
            freq[categories[i]]+=1
        else:
            total[categories[i]]=targets[i]
            freq[categories[i]]=1
    result=[]
    for i in categories:
        mean=total[i]/freq[i]
        result.append(mean)
    return result