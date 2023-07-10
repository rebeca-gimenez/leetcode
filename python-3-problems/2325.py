'''
2325. Decode the Message
Inputs:
    key: string, a cipher key
    message: string, a secret message
The steps to decode message are as follows:
Use the first appearance of all 26 lowercase English letters in key as the 
order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one 
instance of each letter in the alphabet), we have the partial substitution 
table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

26 <= key.length <= 2000
key consists of lowercase English letters and ' '.
key contains every letter in the English alphabet ('a' to 'z') at least once.
1 <= message.length <= 2000
message consists of lowercase English letters and ' '. 
'''
def decodeMessage(key, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    no_dups = {" ": " "}
    count = 0
    for letter in key:
        try:
            if letter not in no_dups and count < len(alphabet):
                #print(letter, alphabet[count])
                no_dups[letter] = alphabet[count]
                count += 1
        except:
            print("error")
    answer = ''
    for letter in message:
        answer += no_dups[letter]
    return answer
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
output = "this is a secret"
print(decodeMessage(key, message), decodeMessage(key, message)==output)


key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
output = "the five boxing wizards jump quickly"
print(decodeMessage(key, message), decodeMessage(key, message)==output)
