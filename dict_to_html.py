from django.template import Template, Context
from django.conf import settings
settings.configure()

news = {'title': ['Bajaj Finance surpasses Axis Bank in m-cap ranking', 'Bajaj Finance surpasses Axis Bank in market-cap', 'Sensex starts on negative note, falls 51 points', 'Why Indian paint makers are shifting to water-based paints'],\
        'domain_rank': [630, 4726, 4381, 1],\
        'spam_score':[1,1,0.6,0.3,0.2]}

n = len(news)
headers_list = [*news]
news_list = list(news.values())
row_list = list(zip(*news_list))
m = len(row_list)

html ="""
<table id="myTable">
    <tr>
        {% for i in range(len(headers_list)) %}
            <th onclick="sortTable(i)">headers_list[i]</th>
        {% endfor %}
    </tr>
    
    {% for i in range(m) %}
        <tr>
            {% for j in range(n) %}
                <td>{{ row_list[i][j] }}</td>
            {% endfor %}
        </tr>
    {% endfor %}
</table>
"""

print(html)