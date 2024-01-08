## Ok here is why
when we develop our python applications we install all our dependencies in a python environment and for deployment most of the time 
we do 

```bash
pip freeze > requirements.txt
``` 
and all the dependencies are packedup in single files, their were lots of method to seperate development dependencies and deployment 
dependencies one is by using pip tools. but i tried to create a simple one 

you just need to have a little knowledge of json 
in this system you are not going to create a requirements.txt file, you will be writing a json file for your requirements 
here is an example 
### JSON  ✨
```json 
{
"Django==5.0":true,
"flake8":false
}
 ```
Cool Cool 
the true and false value help to seperate development and deployment dependencies , true -> for those requirements that are needed 
while deploying your application and false are for those that are needed only in development and are not required in deployment  
run it 

add this proj in your working dir and crete json containing requirements

```bash
python requirement_manager.py <input.json>
```
it will suppoer Yaml format soon 
