import models
import bot

if __name__ == '__main__':
    print("Hello")
    models.initialize_db()
    g = models.BankUser.select()
    for gg in g:
        print(gg.username)
    print(g)
    #bot.run()