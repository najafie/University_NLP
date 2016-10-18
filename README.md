This program is for university Nlp Course. (Dr.Mahdavi)
The program is written in Python language.

To run python script you should be install python IDE.
You can download python IDE in the link below:
https://www.python.org/downloads/release/python-352/

And to debug program and change source can use Pycharm

Download Pycharm in the link below:
http://p30download.com/fa/entry/43943/

////////////////////////////////////////// Tokenization.py Document ////////////////

the Tokenization.py file is 3 function

function Normalization:
This function to performs the Normalization operations

Examples of the operations:

* remove space from begin and end of sentense.
* remove remove extra space in sentense.
* change persian and arabic digit to english digit.
* change number of characters in arabic to persian.( exp : ئ ي   to ی )
* remove character _ in sentense. (exp: مدیــریت to  مدیریت)
* change dot Percent character to Percent (separating point in the sentense) :
    Exp:  14.2  ->  14/2
	Exp:  mitavand.  -- >  mitavanad.
* remove [({}<>»«“] characters in sentense.

function Translation:
this function do the conversion operation.
Examples of the operations:

* change  ب  to b
* change arabic elements:
  َ  : a 
  ُ  : o
  ِ  : e
  ً  : aN
  ٌ  : oN
  ٍ  : eN
  ّ  : #
  ْ  : ×
  
function Tokenization:
this function do the Tokenization operation.
function input argument is : senetense (text)
function output argument is array of tokens.
//////////////////////////////////////////////////////////////////////////////

programing by : hasan najafie

