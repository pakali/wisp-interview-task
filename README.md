# Interview task for hellowisp.com

# Instruction
How to run:

```
docker-compose up
```

Then go to browser http://127.0.0.1/docs and start using API

# Description
Option 2 - Look at the pseudocode below. specialMath(7) returns 79. specialMath(17) returns 10926. This question has two parts: first, implement it in Python, ensuring someone can call it through a REST endpoint (e.g. $> curl http://127.0.0.1:5000/specialmath/7); second, have the endpoint calculate for an input of 90. You can use frameworks such as Django and Flask if you like.

function specialMath(int n) {
	if(n==0) return 0
	else if(n==1) return 1
	else return n + specialMath(n-1) + specialMath(n-2)
}
