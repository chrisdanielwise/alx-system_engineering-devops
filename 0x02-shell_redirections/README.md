#Shell_redirections and commands

1)  	0-hello_world

   	#!/bin/bash
	echo "Hello, World"

2)  	1-confused_smiley

   	#!/bin/bash
   	echo "\"(Ôo)'"


3)   	2-hellofile

   	#!/bin/bash
   	cat /etc/passwd 

4)  	3-twofiles

   	#!/bin/bash
   	cat /etc/passwd /etc/hosts

5)  	4-lastlines

   	#!/bin/bash
   	tail /etc/passwd

6)  	5-firstlines

   	#!/bin/bash
   	head /etc/passwd

7)  	6-third_line

   	#!/bin/bash
   	head --lines=3 iacta | tail --lines=1

8)  	7-file

   	#!/bin/bash
   	echo "Best School" > "\*\\\'\"Best School\"\'\\\*$\?\*\*\*\*\*:)"

9)  	8-cwd_state

   	#!/bin/bash
   	ls -la > ls_cwd_content


10)  	9-duplicate_last_line

    	#!/bin/bash
    	echo -en "" | tail --lines=1 iacta >> iacta


11)  	10-no_more_js

    	#!/bin/bash
    	find . -name '*.js' -type f -delete

12)  	11-directories

    	#!/bin/bash
    	find -mindepth 1 -type d | wc -l

13)  	12-newest_files

    	#!/bin/bash
    	ls -t | head

14)   	13-unique

   	 #!/bin/bash
   	 sort | uniq -u

15)   	14-findthatword

     	#!/bin/bash
     	grep -i root /etc/passwd

16)  	15-countthatword

     	#!/bin/bash
     	grep -i bin /etc/passwd | wc -l

17)   	16-whatsnext

     	#!/bin/bash
     	grep -iA 3 root /etc/passwd

18)    	17-hidethisword

      	#!/bin/bash
      	grep -iv bin /etc/passwd

19)    	18-letteronly

        #!/bin/bash
	grep -i "^[a-z]" /etc/ssh/sshd_config


20)  	19-AZ

	#!/bin/bash
	tr Ac Ze

21)	20-hiago

	#!/bin/bash
	tr -d cC

22)	21-reverse

	#!/bin/bash
	rev

23)	22-users_and_homes

	#!/bin/bash
	cut -d':' -f1,6 /etc/passwd | sort

24)	100-empty_casks

	#!/bin/bash
	find . -empty -printf "%f\n"

25)	101-gifs

	#!/bin/bash
    	find . -type f -name "*.gif" -printf "%f\n"| rev | cut -d '.' -f2- | rev | LC_ALL=C sort -f

26)	102-acrostic

	#!/bin/bash
	cut -c 1 | tr -d '\n' | sort

27)	103-the_biggest_fan

	#!/bin/bash
	tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev


