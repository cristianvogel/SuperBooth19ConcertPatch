130BPM_SuperBooth:
	- CIRKLON	(G 1)	g>	PROK BD		(In)
	- CIRKLON	(G 1)	g>	SSFEntity	(In)
	- CIRKLON	(G 2)	g>	PROK SN		(In)
	- CIRKLON	(G 3)	g>	PROK CP		(In)
	- CIRKLON	(G 4)	g>	PROK HH		(In)
	- CIRKLON	(G 7)	g>	DISTING4	(X)
	- CIRKLON	(G 8)	c>	WORNGMULT	(In1) 
	* CIRKLON:
				| 	Tempo = 130
				|	Song = Booth19
				| 	Drums = 5,6,7,8
				| 	Samplr = 15
				| 	Sync = 16

	- PROK BD 	(Out)	-> 	QUAD VCA 	(In 1)
	- PROK SN 	(Out)	->	QUAD VCA 	(In 2)
	- PROK CP	(Out)	->	QUAD VCA 	(In 3)
	- PROK HH	(Out)	->	QUAD VCA	(In 4)
	
	- QUAD VCA	(Out 1)	->	SISTERS 	(In Low)
	- QUAD VCA	(Out 2)	->	MUTON 		(In 3)
	- QUAD VCA	(Out 3)	->	SVVCF 		(In 2)
	- QUAD VCA	(Out 4)	->	SISTERS 	(In High)

	- WOGGLEBUG (Stpd)  >>	PROK HH 	(X)
	- WOGGLEBUG	(Stpd)	>>	SSFEntity	(FM CV)
	- WOGGLEBUG	(Stpd)	>>	CHDORGAN	(Root) //Optional
	- WOGGLEBUG (Wggl)	>>	PROK SN 	(X)
	- WOGGLEBUG (Smth)	>>	DISTING4 	(Z)	//file selection mod
	- WOGGLEBUG (Smth)	>>	PROK SN 	(Y)	
	- WOGGLEBUG (Brst) 	>>	FLOATING 	(1) [color=yellow, style=dotted]


	- SISTERS	(Centr)	->	MUTON		(In 5)
	- SISTERS	(Low)	->	MUTON		(In 2)
	- SISTERS	(High)	->	MUTON		(In 4)
	
	- WORNGMULT	(Out 1) c>	OCTASRC		(Sync)
	- WORNGMULT	(Out 1) c>	TapoDelay	(Clock)	
	- WORNGMULT	(Out 2)	>>	WOGGLEBUG	(Ext)
	- WORNGMULT	(Out 2)	>>	SVVCF		(CV 1)
	- WORNGMULT	(Out 3)	>>	PROK CP 	(X) 
	- WORNGMULT	(Out 3) >> 	CRUSHmk2	(TIME)

	- OCTASRC	(Out 1)	>>	SISTERS		(FM)
	- OCTASRC	(Out 2)	>>	WORNGMULT	(In 2)
	- OCTASRC	(Out 3)	>>	MULT_1		(1)	
	- OCTASRC	(Out 4)	>>	DISTING4	(Y)
	- OCTASRC	(Out 5)	>>	BLKOUTPUT 	(PAN)
	- OCTASRC	(Out 5) >>	MULT_2		(1)
	- OCTASRC	(Out 6)	>>	SVVCF		(CVIn1)
	- OCTASRC	(Out 7)	>>	PROK CP		(Y)
	- OCTASRC	(Out 8)	>>	MUTON		(CV 5)
	
	- MUTON		(Out 6)	->	TapoDelay	(In)
	- MUTON		(Out 1)	->	BLKOUTPUT	(In 1)
	- MUTON		(Out 8)	->	BLKOUTPUT	(In 3)

	- TapoDelay	(LR)	->	BLKOUTPUT	(In 4)
	- TapoDelay (Gate)	t>	WOGGLEBUG	(Step)
	
	- SSFEntity	(Out)	->	MUTON		(In 1)
	- SSFEntity	(Duck)	>>	TapoDelay	(DryWet)
	
	- DISTING4	(A)		->	MUTON		(In 6)
	- DISTING4	(B)		->	SVVCF		(In 3)
	
	- CHDORGAN	(Out)	->	SISTERS		(In Centr)
	
	- SVVCF		(Mix+)	->	CRUSHmk3	(In)	
	- SVVCF		(Notch)	->	CRUSHmk2	(Return)
	
	- A118		(Rnd)	->	WORNGMULT	(In 3)
	
	- CRUSHmk3	(Out)	->	MUTON		(In 8)
	- CRUSHmk3	(Send)	->	CRUSHmk2	(In)
	- CRUSHmk2	(Send)	->	CRUSHmk3	(Return)
	- CRUSHmk2	(Out)	->	MUTON		(In 7)

	- MULT_1		(2)	>>	MUTON		(CV 6)
	- MULT_1		(3)	>>	CRUSHmk2	(InDlyCV)

	- MULT_2		(2)	>>	PROK BD 	(X)
	- MULT_2		(3)	>>	QUAD VCA	(CV 4) // hats amp mod

	* BLKOUTPUT:
		| 	MainOut = PA

	* DISTING4:
		| 	Algorithm = I1 AudioPlayback
		| 	Card Folders = 6
		| 	Select Folder = P0
		| 	Envelope time = P1
		| 	Change modes = PushZ

	* SISTERS:
		|	Span = 1pm
		|	Quality = 7:30pm
		| 	Switch = Formant (preferred)

	* FLOATING:
		| 	TapoDelay: TapIn	
		| 	Disting: Trig-Y

