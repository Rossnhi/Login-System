player = input("Choose x or o:\n")
if player != "x" or player!= "o":
        player = input( "Not correct input. Choose x or o only.\n")
if player == "x":
	comp = "o"
else:
	comp = "x"
board = [[1,2,3],[4,5,6],[7,8,9]]
board_display ="1|2|3\n4|5|6\n7|8|9"
while True:
	player_turn = input("Type the number corresponding to the postion you want to mark.\n"+ board_display + "\n")
	if player_turn:
		board_display = board_display.replace(player_turn,player)
		
	
		
