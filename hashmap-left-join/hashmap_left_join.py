from data_structures_and_algorithms.hashtable import Hashtable





def left_join(map1,map2):
    arr=[]
    get_map2=None
    for key in map1.keys():
        if map2.contains(key):
          get_map2=map2.get(key)  
        arr.append([key,map1.get(key),get_map2])
        get_map2=None



    return arr




if __name__=="__main__":
    h1=Hashtable()
    h1.set('diligent','employed')
    h1.set('fond','enamored')
    h1.set('guide','usher')
    h1.set('outfit','garb')
    h1.set('wrath','anger')

    
    h2=Hashtable()
    h2.set('diligent','idle')
    h2.set('fond','averse')
    h2.set('guide','follow')
    h2.set('flow','jam')
    h2.set('wrath','delight')
    
    print(left_join(h1,h2))

