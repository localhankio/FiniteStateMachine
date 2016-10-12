Henry Shen
27 September 2016
CSC 470 NLP
Language Implementation: Python 3.5.2

Instructinons to run Project1
	
	Deliverables 1 - 3:
	These deliverables are called FiniteStateMachine1, 2, and 3 respectively. These programs all must take one argument which is the string to be processed by the FSA. It will output "Matched" if the string matches, and "reject if it does not." Further, they read the FSA information (states, transition table, etc.) from a folder called "sheepLanguageMachine" that should be in the same directory as the FiniteStateMachines. That subdirectory and the files in it are the same files given to us as test cases. 

	Example:
		$ py FiniteStateMachine1.py baa!
		$ **************************
	 	$  Accepted  baa!
	    $ **************************

		$ py FiniteStateMachine2.py asfsdfsbaaa!
		$ **************************
	 	$ Accepted  baaa!
		$ **************************

		$ py FiniteStateMachine3.py baa!
		$ **************************
		$ Accepted  baa!
		$ **************************

		$ py FiniteStateMachine2.py asfsdfsbaaa!sdfasf
		$ ***** Rejected *****

	For Deliverable 4, the project file is called FiniteStateMachine4.py and read files from a subdirectory called "D4_Machine." It also must only take one argument: the string to be compared against the implemented FSA. Again, FSA 4 should be in the same directory as the folder that contains the information for the FSA. D4_Machines contains the following:
		1) alphabet.txt
		2) finalStates.txt
		3) startState.txt
		4) states.txt
		5) transitionTable.txt

	FiniteStateMachine4 will read these files and use store the information in each for the FSA. 

	NOTE: The FiniteStateMachine 1 - 3 only work with the sheep language. FiniteStataMachine 4 is more generalizable and will work for FSAs that have more than one final state. 
		  For example, if the final state in the sheep language could accept any amount of "!"s, FiniteStateMachine 4 would properly accept it. 