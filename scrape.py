import requests
from bs4 import BeautifulSoup


url = "http://fartoncat.000webhostapp.com"
#url = "https://www.google.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
#download and save html file
print("HTML copied")
print("Writing HTML")
f = open("index.html", "wb")
f.write(soup.prettify('utf-8'))
f.close()
print("HTML saved")
print(' ')
#style sheet check and DL
def stylecheck(content):
    check = content.find('link', attrs={'rel':'stylesheet'});
    if(check == None):
        return False
    else:
        return True
def getstylename(content):
    stylestring = content.find('link', attrs={'rel':'stylesheet'});
    style = stylestring.get("href")
    return style

if(stylecheck(soup)):
    print()
    urlstyle = url + '/' + getstylename(soup)
    rstyle = requests.get(urlstyle)
    style = BeautifulSoup(rstyle.content, 'html.parser')
    print("style sheet found and copied")
    #write style to css file
    f = open("style.css", "wb")
    f.write(style.prettify('utf-8'))
    f.close()
    print("Style sheet writen and saved")
else:
    print("no style sheet")


#find lists
print(' ')
licount = 0
for li in soup.find_all('li'):
    licount += 1
print('site has {} Lists'.format(str(licount)))#print total amount if li tags there are
#find links
hrefcount = 0
for href in soup.find_all(href=True):
    hrefcount += 1
print('site has {} hrefs'.format(str(hrefcount)))#print total amount of href links there are

#javascript related
print("Searching for inline js and external js files")
jscount = 0
inline = 0
external = 0
jssrc = []
for js in soup.find_all('script'):
    jscount += 1
    #check to see if the script has a src attribute
    if(js.has_attr('src')):
        #if it has a src value its an external js file
        external += 1
        jssrc.append(js['src'])
    else:
        #else is written in the html file
        inline += 1
print("site has {} script tags".format(str(jscount))) #total script tags
print('site has {} external script files-'.format(str(external))) #how many with src
for i in jssrc:
    print( '    {}'.format(str(i)))#src value
print('site had {} inline scripts'.format(str(inline)))#how many without src





















#jj
