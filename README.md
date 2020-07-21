# Contact list webscraping from GuiaMais website

  The program performs an automation with Selenium that enters the site 'https://www.guiamais.com.br/manaus-am' and searches for the type of establishment given by the user in the input. Then, the Selenium webdriver finds all the corresponding establishments and starts searching for the html on their contact pages.
  
  The html of each contact page is analyzed with BealtifulSoup, which returns the values of: establishment's name, address and telephone numbers.
  
  The data is placed in a dictionary that later becomes a Pandas dataframe, which at the end converts to a .csv file.
