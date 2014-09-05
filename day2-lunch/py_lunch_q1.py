<<<<<<< HEAD
#!/usr/bin/env python
=======
#!/usr/bin.env python
>>>>>>> 0b296dc1145c781656b6cc9a570b79f873659487

number_alignments_sam = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(number_alignments_sam)

n_al = 0
while True:
    line = f.readline()
    if line == "":
        break
    else:
        n_al = n_al + 1
<<<<<<< HEAD
print n_al
=======
print n_al
>>>>>>> 0b296dc1145c781656b6cc9a570b79f873659487
