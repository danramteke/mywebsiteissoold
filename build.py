import yaml
import mako
from mako.template import Template

with open('data.yml') as data: 
    tweets = yaml.load(data.read())['tweets']

#print tweets
print Template("""
here are some tweets:
% for tweet in tweets:
- ${tweet['text']}
% endfor
""").render(tweets=tweets)
