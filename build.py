import yaml
import mako
from mako.template import Template

with open('data.yml') as data: 
    tweets = yaml.load(data.read())['tweets']

#print tweets
print Template("""
<html><head><title>My Website is so Old</title>
<style type="text/css">
body, li, a, div {
  font-family: Helvetica, sans-serif;
}
body {
margin-left: auto; margin-right: auto;
width:90%;
}

li {
  margin-top: 5px;
  margin-bottom: 30px;
  background-color: #dddddd;
  padding: 8px;
}

a{
display:block;
font-size: smaller;
text-align:right;
}

div.quote {
background-color: white;
padding: 8px;
margin-bottom:8px;
}

ol {
list-style-type: none;
}

h1, h2 {
display: block;
text-align: center;
}

</style>
</head>

<body>
<h1>My Website is so Old</h1>
<h2>An Unillustrated Mockularity</h2>

<ol id="list_o_tweets">
% for tweet in tweets:
  <li>
    <div class="quote">${tweet['text']}</div>
    <a href="${tweet['url']}">Original</a>
  </li>
% endfor
</ol>

</body>
</html>
""").render(tweets=tweets)
