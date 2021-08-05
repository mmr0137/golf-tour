import requests, bs4

for i in range(1,31):
	# Get the webpage
    resp = requests.get('http://localhost:8000/golfer/'+str(i))
    
    if resp.status_code == 200:
        # Create Beautiful Soup object with all the text from the webpage
        golfer = bs4.BeautifulSoup(resp.text, "html.parser")
        
        # Get the golfer name from h2 element
        golfer_name = golfer.find('h2').text.strip()
        print("Golfer: " + golfer_name + '\n')
        # Create a list of td elements for the scores
        td_list = golfer.select('td')
        # Loop through the td_list
        for index in range(0, len(td_list), 2):
            tourn_name = td_list[index].getText().strip()
            tourn_score = td_list[index+1].getText().strip()
            row = tourn_name.ljust(21) + " " + tourn_score
            print(row)
            if index == 0:
                print("----------".ljust(21) + " " + "----------")
    print("=====================\n")

