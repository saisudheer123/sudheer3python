inp=raw_input()
if(inp>='a' and inp<='z') or (inp>='A' and inp<='Z'):
    if inp in ['a','e','i','o','u','A','E','I','O','U']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
