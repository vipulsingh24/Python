from jinja2 import Template
template = Template(open('template-jinja2.html').read())

news = {'title': ['Bajaj Finance surpasses Axis Bank in m-cap ranking', 'Bajaj Finance surpasses Axis Bank in market-cap', 'Sensex starts on negative note, falls 51 points', 'Why Indian paint makers are shifting to water-based paints'],\
        'domain_rank': [630, 4726, 4381, 1],\
        'spam_score':[1,1,0.6,0.3,0.2]}

# n = len(news)
headers_list = [*news]
news_list = list(news.values())
# row_list = list(zip(*news_list))
# m = len(row_list)
rows = list(zip(*news_list))

open('output.html', 'w').write(template.render(
	header = headers_list,
    rows = rows
))

