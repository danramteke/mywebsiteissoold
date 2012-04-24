import yaml
import mako
from mako.template import Template

with open('data.yml') as data: 
    tweets = yaml.load(data.read())['tweets']

#print tweets
print Template("""
<html><head><title>My Website is so Old</title>

<body>

<h1>My Website is so Old</h1>
<h2>An Unillustrated Mockularity</h2>

<div id="list_o_tweets">
% for tweet in tweets:
  <div class="box">
    <div class="quote">
      ${tweet['text']} 
   </div>
  </div>
% endfor
</div>

</body>
</html>
""").render(tweets=tweets)
