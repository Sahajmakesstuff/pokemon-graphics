#Pokemon with Graphics
An attempt to make a pokemon game with graphics using the tkinter method for python

#Features:
1. We should be able to choose a pokemon from:
	a. leafy (grass)
	b. flamey (fire)
	c. bubbly (water)

2. The Pokemon will have stats which will be displayed below the button for choosing

3. If we click the button for the specific pokemon, it gets added to out party

4. We can fight trainers who have different pokemon (currently 5 to choose from)
	a. beetlebug (bug)
	b. misteon (fairy)
	c. earthborn (ground)
	d. birdy (flying)
	e. nasty (dark)

5. Each pokemon will have 4 moves to choose from

6. If we win, we can choose to either continue or retire and then it will display our score

7. if we defeat 5 trainers, we win

#Stat Calculation
1. Each pokemon has 6 stats
	a. hp
	b. attack
	c. defence
	d. special attack
	e. special defence
	f. speed

2. Stat Calculation is done as follows:
	a. HP = [(2 * base + IV)/100] + lvl + 10 to nearest whole number != 0
	b. Other stats = [(2 * base + IV + lvl) / 100] + 5 * nature boost to nearest whole number != 0

3. Each stat can be altered (boosted or lowered) to +6 or -6 (except hp)

	a. +1 --> * 1.5
	b. +2 --> * 2
	c. +3 --> * 2.5
	d. +4 --> * 3
	e. +5 --> * 3.5
	f. +6 --> * 4

	g. 0 --> normal

	h. -1 --> * 0.66
	i. -2 --> * 0.5
	j. -3 --> * 0.4
	k. -4 --> * 0.33
	l. -5 --> * 0.28
	m. -6 --> * 0.25

#Damage Calculation
1. If move is physical, then physical attack of attacker and physical defence of defender would be used

2. If move is special, then special attack of attacker and special defence of defender would be used

3. Damage = (((((2 * lvl) / 5) + 2 * power * A / D) / 50) + 2) * Critical * random * STAB * type

4. 1/16 chance to crit which makes damage 1.5 X

5. Random is a value between 0.8 and 1

6. STAB is if same type then 1.5 X damage

7. type is if super effective then 2 X damage and not very effective then 0.5 X damage

