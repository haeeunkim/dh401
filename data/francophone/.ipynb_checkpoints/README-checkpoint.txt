The columns are separated by a \t
column 1: recipx (if 0 or strinng there is an error)
column 2: break (0->no break, 1 ->beginning of sentence, 2->beginning of small sentence)

column 3: rhyme (0->no rhyme, 1->rhyme)

column 4: lyric (R-> rest)

*>Verse1 *>Verse1 *>Verse1 *>Verse1 -> beginning of a new verse with verse number
	-> If more than 3 successive rests, it makes a new verse 

=1 =1 =1 =1 -> beginning of a new measure with measure number

For the XML:
G-> recipx (Surface)
A-> Break (beginning of sentence)
B-> Break2 (beginning of a small sentence)
D-> Rhyme
C-> False rest (add to the duration of the previous note)

<Chord> -> in chord with the previous G (surface) note
