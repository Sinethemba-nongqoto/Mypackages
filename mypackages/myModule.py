def top_n(items, n):
    """ Returns to top n items in an array, in desceding order.
    
    args:
        items(arrays) : list or array- like object.
        n(int) : the number of items to return
        
    return:
        array: n items in desc order
        
    Egs:
        >>> top_n([8,9,3,4,7,2,0], 3)
        [9,8,7]
    """
    for i in range(n): # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j]>items[j+1]: #if this item is bigger than the next item...
                items[j], items[j+1]= items[j+1],items[j] #swap the two
                
    #get the last two items
    top_n = items[-n:]
    
    #returns in descending order
    return top_n[::-1]  