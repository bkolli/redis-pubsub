import redis
import datetime
import time

def main():
	r = redis.client.StrictRedis()
	i = 0
	while True:
		print 'Sending====>  {0}'.format(i)
		i+=1
		r.publish('data', i)
		time.sleep(1)

if __name__ == '__main__':
	main()
