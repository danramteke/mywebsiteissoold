import yaml
import mako
from mako.template import Template

with open('data.yml') as data: 
    tweets = yaml.load(data.read())['tweets']

#print tweets
print Template("""
<html><head><title>#mywebsiteissoold</title>
<style type="text/css">
div, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, p, blockquote, table, th, td, embed, object {
padding: 0;
margin: 0; 
}

body {
padding: 9px;
margin: 21px;
}

body, li, a, div {
  font-family: HelveticaNeue, Helvetica, sans-serif;
}

li {
  margin-top: 5px;
  margin-bottom: 31px;
  background-color: #ffffff;
  padding: 9px;
  border: 9px #dddddd solid;
  font-size: 1.5em;
}

a{
text-decoration: none;
color: black;
}

ol {
margin-top:31px;
list-style-type: none;
list-style-position: outside;
}

h1, h2 {
display: block;
}

div#attribution {
font-size: 0.75em;
}

</style>
</head>

<body>
<h1>#mywebsiteissoold</h1><h2>An Unillustrated Mockularity</h2>

<ol id="list_o_tweets">
% for tweet in tweets:
  <li><a href="${tweet['url']}">${tweet['text']}</a></li>
% endfor
</ol>

<div id="attribution">Created by <a href="http://danramteke.com">Dan Ramteke</a>, &copy;2012</div>
</body>
</html>
""").render(tweets=tweets)
