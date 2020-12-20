# password-pawn-checker
Using the api from the pwnedpasswords.com , check how many times this password has been pawned.

To achieve this, I've noted the below steps as I've understood

"Step1:
To build a password checker…
a website which provides pawned password count from leaks eg have I been pawned..we need that API and to it we need to send the password…calling ApI via the request module

https://api.pwnedpasswords.com/range/{first 5 hash chars}"

"Step2:
Now, we cant send our password like this to any website..>DON’T TRUST anyone, infact even storing a password of user into our DB…so first its should be hashed up/making it gibberish…SHA1 hash function is one of eg"

"Step3:
Hash Tables...
Hash function takes the key and converts it into gibberish/hashed and this is mapped to a memory address where we want to store data/ value

Hash function have to do a compelx job n they are optimized a lot"

"Step4:
To the API we only need to send the first 5 characters of the hashed up password and remaining tail can be kept separate.

In the response of the API we need to get in a way to hcheck each line for the tail…when the tail matches…that’s our exact match for password and the count against it is the count how many times its been used"

Note: To have hashing …we can use the hashlib module…sha1() function and hexdigest() for retrieving value as only hexadecimal digits and We have to use utf-8 encoding.


Credit to Zero to mastery course from Andrei Neagoi.


