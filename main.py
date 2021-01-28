import tick


def main():
    my_game = tick.Tick()
    my_game.thread_1.start()
    my_game.main_loop()


if __name__ == "__main__":
    main()
