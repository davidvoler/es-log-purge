from datetime import date, timedelta
import requests

def get_days_ego(days_ego,es_host="http://localhost:9200", prefix='logstash-', max_history=365):
  for i in range(days_ego, max_history):
    date_index = date.today() - timedelta(i)
    idx = "{}{}".format(prefix, date_index.strftime('%Y.%m.%d'))
    url = "{}/{}".format(es_host,idx)
    r = requests.delete(url)
    print(r.status_code)


if __name__ == "__main__":
  get_days_ego(20)