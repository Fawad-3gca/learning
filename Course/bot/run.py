from booking.booking import Booking

# with Booking(teardown=True) as bot:
#     bot.land_first_page()
#     bot.change_currency(currency="USD")
#     bot.select_place_to_go('New York')
#     bot.select_dates(check_in_date='2022-07-01',
#                      check_out_date='2022-07-02')
#     bot.select_adults(10)
#     bot.click_search()
#     bot.apply_filtrations()


try:
    with Booking(teardown=True) as bot:
        bot.land_first_page()
        bot.change_currency(currency="USD")
        bot.select_place_to_go(input("Where you want to go ?"))
        bot.select_dates(check_in_date=input("What is the check in date ?"),
                         check_out_date=input("What is the check out data ?"))
        bot.select_adults(int(input("How many people ?")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()  # A workaround to let our bot to grab the data properly
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%; C:path-to-your-folder \n\n'
        )
    else:
        raise
