from flask import Flask
import redis
# create an app instance
app = Flask(__name__)

#redis_host = "localhost"
redis_host = "redis-server"
redis_port = 6379
redis_password = ""
r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
r.set("visits", 0)

# at the end point "/" call method "hello_redis", which returns the number of visits
@app.route("/")
def hello_redis():
    try:  
        visits = r.get("visits")
        r.set("visits", int(visits) + 1)
        return "Number of visits is: " + str(visits) 
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"),debug=True)