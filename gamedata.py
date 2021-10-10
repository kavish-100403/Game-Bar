def gamesui():
    while True:
        user_input = int(input("Games: \n 1.Flappy Bird \n 2.Snake Game \n 3.Pong \n 4.Stone Paper Scissors \n Enter Your choice:"))
        if user_input == 1:
            import flappybird
            flappybird.flappy_bird()
            break

        if user_input == 2:
            import OG
            OG.snake_game()
            break

        if user_input == 3:
            import pong
            pong.pong_game()
            break

        if user_input == 4:
            import sps
            sps.sps_game()
            break

        else:
            print("Please enter from the above choice \n")
            
        
