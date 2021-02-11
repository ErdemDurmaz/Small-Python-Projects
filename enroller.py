print("Scraping data from web...")
enrollment = {'Lecture Code database':"z04-17a", 'Time database':"Wednesday-11:15",
'Lecture Code  datawarehouses':"z04-68a", 'Time datawarehouses':"friday 9.15",
'Lecture Code  Distrubuted_computer_systems':"z04-73a", 'Time Distrubuted_computer_systems':"9:15 Tuesday",
'Lecture Code  Artificial_Intellegence':"z04-66a", 'Time Artificial_Intellegence':"Thursday 13.15"}
for k,v in enrollment.items():
    print (str(k) + ' ' + str(v))