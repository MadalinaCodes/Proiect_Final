Proiect Testare Automată


Structura proiectului? 

	În  features sunt scenariile de test
	În Steps sunt acțiunile făcute de utilizator
	În Pages sunt selectori, micro acțiuni și eventuale validări
	În Scripts sunt niște teste simple pe lângă cele din scenariile de test
	-browser.py-  creează clasa Browser cu inițializarea browserului și a waiturilor
	-context.py- conține 2 metode
		una care se apelează înainte de fiecare test
		Și alta care se apelează după fiecare test
	În -cmd- avem ordinea comenzilor din Terminal
	-behave.ini- fișier simplu pentru interpretarea testelor în rapoarte html
