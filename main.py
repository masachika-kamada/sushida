from driver import ChromeDriver


def main():
    driver = ChromeDriver()
    driver.access_sushida()
    driver.play_game()


if __name__ == "__main__":
    main()
