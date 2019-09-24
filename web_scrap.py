from urllib.request import urlopen
from bs4 import BeautifulSoup

print('Hello there ! ')
companies = ['NBK','Warba Bank','Ooredoo','Zain']

no=1
for comp in companies:
    print("{}. {}".format(no,comp))
    no += 1

choice=int(input("Chose one of these companies and get it's stock information. "))


if choice == 1:
    print('You choose NBK.')
    html = urlopen("https://english.mubasher.info/markets/BK/stocks/NBK")
    soup = BeautifulSoup(html.read(), 'html.parser')

    CP = soup.find('div', {'class':'market-summary__last-price'})
    V = soup.find_all('span', {'class':'market-summary__block-number'})[4]
    MC = soup.find_all('span', {'class':'number number--aligned'})[1]
    print('Closing Price: %s ' % CP.get_text())
    print('Volume: %s ' % V.get_text())
    print('Market Cap: %s Kuwaiti Dinar' % MC.get_text())


elif choice == 2:
    print('You choose Warba Bank.')
    html = urlopen("https://english.mubasher.info/markets/BK/stocks/WARBABANK")
    soup = BeautifulSoup(html.read(), 'html.parser')

    CP = soup.find('div', {'class':'market-summary__last-price'})
    V = soup.find_all('span', {'class':'market-summary__block-number'})[4]
    MC = soup.find_all('span', {'class':'number number--aligned'})[1]
    print('Closing Price: %s ' % CP.get_text())
    print('Volume: %s ' % V.get_text())
    print('Market Cap: %s Kuwaiti Dinar' % MC.get_text())


elif choice == 3:
    print('You choose Ooredoo.')
    html = urlopen("https://english.mubasher.info/markets/BK/stocks/OOREDOO")
    soup = BeautifulSoup(html.read(), 'html.parser')

    CP = soup.find('div', {'class':'market-summary__last-price'})
    V = soup.find_all('span', {'class':'market-summary__block-number'})[4]
    MC = soup.find_all('span', {'class':'number number--aligned'})[1]
    print('Closing Price: %s ' % CP.get_text())
    print('Volume: %s ' % V.get_text())
    print('Market Cap: %s Kuwaiti Dinar' % MC.get_text())


elif choice == 4:
    print('You choose Zain.')
    html = urlopen("https://english.mubasher.info/markets/BK/stocks/ZAIN")
    soup = BeautifulSoup(html.read(), 'html.parser')
    CP = soup.find('div', {'class':'market-summary__last-price'})
    V = soup.find_all('span', {'class':'market-summary__block-number'})[4]
    MC = soup.find_all('span', {'class':'number number--aligned'})[1]

    print('Closing Price: %s ' % CP.get_text())
    print('Volume: %s ' % V.get_text())
    print('Market Cap: %s Kuwaiti Dinar' % MC.get_text())


else:
    print('You have entered a wrong input!')