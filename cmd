BDD = behaviour driven development
# selenium este toolul care ne ajuta sa interactionam cu browserul
pip install -U selenium
sau
py -m pip install -U selenium # -U vine de la upgrade, poate fi pus peste tot
#   behave e ca un lipici care ne ajuta sa interpretam proiectul cum avem nevoie
pip install behave # instalam o librarie care ne ajuta sa ne facem frameworkul asta de behaviour driven development
pip install behave-html-formatter # ne ajuta sa facem rapoartele

run test
behave -f html -o behave-report.html --tags=smoke # cerem librariei behave sa ruleze toate testele cu tag-ul smoke si sa genereze un raport html care sa se numeasca behave-report

behave -f help
behave -f html
behave -f html -o behave-report.html


