# box-office-mojo-scraper
[Box Office Mojo](www.boxofficemojo.com) is a bit tricky when it comes to extracting data since there are tables nested on each movie's profile page. The Python code in this repository provides a way to extract the information on the profile page of the movies listed on the site. An example of the information that is pulled is available in the figure below, pertaining to the release of [Big Hero 6](http://www.boxofficemojo.com/movies/?id=disney2014.htm).

<p align="center">
<img src="https://cloud.githubusercontent.com/assets/16767381/12499596/f3b84696-c079-11e5-9501-c3bed4f26519.png" width="400">
</p>

```
MojoLinkExtract.py
```
Extracts the links for each movie profile page (approx 16,101) and writes them as comma separated strings into MovieLinks.txt.
```
MovieLinks.txt
```
Comma separated strings for each partial movie link to box office mojo. Must be preceded with `http://www.boxofficemojo.com`.
```
MojoMovieData.py
```
Extracts movie data in the example image above.
