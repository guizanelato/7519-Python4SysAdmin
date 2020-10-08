
from redis import Redis

SESSION_TYPE = 'redis'
SESSION_REDIS = Redis(host='200.100.50.90', port=6379, password='Redis2019!')
