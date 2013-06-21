
from com.prashanth.datamodels.UserData import MovieDetails
import re
import urllib
totalUrl = []

yearsToScrap = range(2000, 2012)
yearsToScrap.append("1990s")
yearsToScrap.append("1980s")

for currentno in yearsToScrap:
    starturl = "http://www.tube.manatelugumovies.net/search/label/" + str(currentno) + "?max-results=100"
    totalUrl.append(starturl)

counter = 0;
# moviefilehandler = open("movieslist.txt", "w+")

def main():
    x = 1
    counter = 0;
    while x == 1:
#        print str(counter)+"---"+str(len(totalUrl))
        if counter == len(totalUrl):
            break
        currentUrl = totalUrl[counter]
#        print currentUrl
        outdata = extractDataFromUrl(currentUrl)
        nextLink = extractNextPageLink(outdata)
        if(nextLink):
            totalUrl.append(nextLink)
            extractRequiredDataFromUrl(outdata)
        counter = counter + 1   

 
def extractNextPageLink(urlData):
    nextUrlMatch = re.search('class\=\'blog\-pager\-older\-link\' href\=\'([^\']*)', str(urlData))
    if(nextUrlMatch):
        return nextUrlMatch.group(1)

    
def extractRequiredDataFromUrl(urlData):
    splittedData = urlData.split('[postlink]')
    if (len(splittedData) > 0):    
        for eachData in splittedData:
            moviedetails = MovieDetails()
            if(eachData.startswith('http')):
                title = re.search(r'<a[^>]*>([^<]*)', eachData)
                if(title):
                    movieTitle = title.group(1)
                    splittedMovieTitle = re.split(r'[()]', str(movieTitle))
                    if(len(splittedMovieTitle) > 0):
                        moviedetails.movieName = splittedMovieTitle[0]
                        moviedetails.movieTrendingCount = 0
                        try:
                            moviedetails.movieYear = int(re.sub(r'\D+', '0', splittedMovieTitle[1]))
                        except IndexError: 
                            moviedetails.movieYear = 0     
                    else:
                        moviedetails.movieName = title.group(1)
                        moviedetails.movieTrendingCount = 0
                        moviedetails.movieYear = 0
#                    print title.group(1) + "\t",
                links = re.findall(r'src="([^"]*)', eachData, re.DOTALL)
                if(len(links) > 0):                
                    if(len(links) == 1):
                        moviedetails.movieImage = "noimage"
                        moviedetails.movieLink = links[0]
#                        moviefilehandler.write("noimage" + "\t" + links[1] + "\n")
#                        print "noimage" + "\t" + links[0]
                    else:
                        moviedetails.movieImage = links[0]
                        moviedetails.movieLink = links[1]
#                        moviefilehandler.write(links[0] + "\t" + links[1] + "\n")
#                        print links[0] + "\t" + links[1]
#                else:
#                    moviefilehandler.write("\n")
#                    print ""       
                moviedetails.put()
            

# # Version that uses try/except to print an error message if the
# # urlopen() fails.
def extractDataFromUrl(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
            return ufile.read()
    except IOError:
        return 'problem reading url:', url


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
    
    
    
