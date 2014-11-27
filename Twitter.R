#--------------------------#
#   Stream Twitter Data    #
#                          #
#     Jeremy Pernicek      #
#         9/30/2014        #
#--------------------------#
## Not run: 

## An example of an authenticated request using the ROAuth package,
## where consumerkey and consumer secret are fictitious.
## You can obtain your own at dev.twitter.com
library(ROAuth)
requestURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "http://api.twitter.com/oauth/access_token"
authURL <- "http://api.twitter.com/oauth/authorize"
consumerKey <- ""
consumerSecret <- ""
my_oauth <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret, requestURL=requestURL,
                             accessURL=accessURL, authURL=authURL)
my_oauth$handshake(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl"))
filterStream( file="tweets_rstats.json",
              track="rstats", timeout=3600, oauth=my_oauth )

## capture 10 tweets mentioning the "Rstats" hashtag
filterStream( file.name="tweets_rstats.json",
              track="rstats", tweets=10, oauth=my_oauth )

## capture tweets published by Twitter's official account
filterStream( file.name="tweets_twitter.json",
              follow="783214", timeout=600, oauth=my_oauth )

## capture tweets sent from New York City in Spanish only, and saving as an object in memory
tweets <- filterStream( file.name="", language="es",
                        locations=c(-74,40,-73,41), timeout=600, oauth=my_oauth )

## capture tweets mentioning the "rstats" hashtag or sent from New York City
filterStream( file="tweets_rstats.json", track="rstats",
              locations=c(-74,40,-73,41), timeout=600, oauth=my_oauth )


## End(Not run)