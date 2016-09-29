Henry Shen
27 September 2016
Language Implementation: Python 3.5.2

FiniteStateMachine4.py reads files from a subdirectory called "D4_Machine." It also must only take one argument: the string to be compared against the implemented FSA. Again, FSA 4 should be in the same directory as the folder that contains the information for the FSA. D4_Machines contains the following:
		1) alphabet.txt
		2) finalStates.txt
		3) startState.txt
		4) states.txt
		5) transitionTable.txt
	The FiniteStateMachine accepts (in regex form): /(ho){3}+!+e?/. Meaning that it wil accept at least three "ho"s and an unlimited amount of "!." 
	FiniteStateMachine4 will read these files and use store the information in each for the FSA. 

	Example:
		$ py FiniteStateMachine4.py hohoho!
		$ **********************
		$ Matched hohoho!
		$ **********************
		
		$ py FiniteStateMachine4.py hohohohoho!
		$ **********************
		$ Matched hohohohoho!
		$ **********************	

		$ py FiniteStateMachine4.py hohohohoho!!!!!
		$ **********************
		$ Matched hohohohoho!!!!!
		$ **********************

		$ py FiniteStateMachine4.py hohohohoho!!!ho
		$ ***** Rejected ******

	NOTE: The FiniteStateMachine 1 - 3 only work with the sheep language. FiniteStataMachine 4 is more generalizable and will work for FSAs that have more than one final state. 
		  For example, if the final state in the sheep language could accept any amount of "!"s, FiniteStateMachine 4 would properly accept it. 