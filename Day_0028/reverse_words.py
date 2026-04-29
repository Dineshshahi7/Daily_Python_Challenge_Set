def reversewords(s):
    # Step 1: split by dot
    words = s.split('.')
        
    # Step 2: remove empty strings
    words = [w for w in words if w]
        
    # Step 3: reverse words
    words.reverse()
        
    # Step 4: join with single dot
    return ".".join(words)
    
    
    
words = "i.like.this.program.very.much"
print(reversewords(words))