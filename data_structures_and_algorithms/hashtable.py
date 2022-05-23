

class Hashtable(object):
    def __init__(self, size=1024):
        self.size=size
        self.map=[None]*size
    
    def hash(self, key):
        ascii_sum= 0
        for ch in key:
            ch_ascii=ord(ch)
            ascii_sum+= ch_ascii
        hashed_key_indx= (ascii_sum*17)%self.size
        return hashed_key_indx

  

    def set(self,key,value):
        indx=self.hash(key)
        if self.map[indx] is None:
            self.map[indx]=[[key,value]]
        else:
            self.map[indx].append([key,value])

    def get(self,key):
        indx=self.hash(key)
        if self.map[indx]==None:
            raise Exception("key is not in the hashtable")
        if len(self.map[indx])==1:
            return self.map[indx][0][1]
        else:
            
            for item in self.map[indx]:
                
                if item[0]==key:
                    
                    return item[1]
    
    def contains(self,key):
        indx=self.hash(key)
        if self.map[indx]==None:
            return False
        if len(self.map[indx])==1:
            if self.map[indx][0][0]==key :
                return True
            else:
                return False
        else:
            
            for item in self.map[indx]:
                
                if item[0]==key:
                    
                    if item[1] :
                        return True
            else: 
                return False


    def keys(self):
        keys=[]
        
        for item in self.map:
            if item:
                if len(item)==1:
                    keys.append(item[0][0])
                else:
                    for i in item:
                        keys.append(i[0])
            
        return keys

def repeated_word(text):
    h=Hashtable()
    if text is None:
        raise Exception("invaled input")

    for word in text.split() :
        
        if h.contains((word.lower()).split(",")[0]):

            return word
        else: 
            h.set((word.lower()).split(",")[0],0)



if __name__=="__main__":
    h= Hashtable()
    h.set('julia', 'Has')
    h.set('uljia', 'hass')
    h.set('salim', 'anwar')
    print(h.keys())
    print(h.hash('julia'))
    #print(h.map)
    #print(h.get('julia'))
    #print(h.get('salim'))
    #print(h.contains('julai'))
    #print(h.keys())

    print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))

        



