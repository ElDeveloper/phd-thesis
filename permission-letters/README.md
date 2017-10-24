# Permission Letters

This directory includes a Python script and a Latex template to generate a
collection of letters to request permission from co-authors. This script relies
on two files `papers.txt` and `co-authors.txt`.

`papers.txt` includes a list of all the papers you co-authored, and their
authors. Example of the file:

```
J. Doe, J. Appleseed. ``Community insights'', \emph{Journal of Chickenology}, 1, 2014.
J. Doe, Q. Pearson, B. Patterson. ``What cannot be learnt through research'', \emph{Journal of Chickenology}, 1, 2014.
```

`co-authors.txt`, is a comma-separated file with co-author lastnames, names and
e-mails.

```
last_name,first_name,email
"Doe","Jane",jane@ucsd.edu
"Appleseed","John",jappleseed@ucsd.edu
"Pearson","Quin",qpearson@ucsd.edu
"Patterson","Becca",bpatterson@ucsd.edu
```

Both of these files are used to produce per-author letters for listing the
publications where you were co-authors. The lookup is done through the last
name of the authors, therefore if you have co-authors with repeated last names
this script will attribute more papers to each author.

