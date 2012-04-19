import yaml
with open('data.yml') as data: 
    tweets = yaml.load(data.read())['tweets']


print tweets
