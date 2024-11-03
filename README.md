# substitution-cypher
A pair of Python programs, to code and decode using an alphabet-substitution cypher

When encoding, first a randomized cypher is presented, then the encoded lines.   Only letters of the alphabet are affected, the rest passes through.

When decoding, the first line input must be the cypher string, already presented from "coder.py", then each line is printed decoded after it is entered.

best used with file redirection and piping of the input and output, i.e.

type filetocode.txt | coder > codedfile.txt
type codedfile,txt | decoder > decodedfile.txt
