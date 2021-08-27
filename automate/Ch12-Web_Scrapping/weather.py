import webbrowser
import sys

city = {'NewTaipei': '65', 'Taipei': '63', 'Taoyuan': '68',
        'Taichung': '66', 'Tainan': '67', 'Kaosiung': '64'}
if len(sys.argv) > 1:
    # Get address from command line.
    searchPlace = sys.argv[1]
    address = 'County.html?CID=' + city[searchPlace]
else:
    # Get address of all cities.
    address = 'index.html'

webbrowser.open('https://www.cwb.gov.tw/V8/C/W/County/' + address)
