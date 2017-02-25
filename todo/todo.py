import sys
import os
import json
import datetime
import io

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

os.chdir("data/") #this will change directory to db directory 

try:
	if( sys.argv[1] == 'create' ):
		if os.path.exists(sys.argv[2] + '.json'):
			print('Already exits!!!')
		else:
			data = os.open(sys.argv[2] + '.json', os.O_CREAT)
			open(sys.argv[2] + '.json', 'w').write('{}')
	
	elif( sys.argv[1] == 'add' ):
		if os.path.exists(sys.argv[3] + '.json'):
			#add an item
			print("{} added to {}".format(sys.argv[2], sys.argv[3]))
			with open(sys.argv[3] + '.json') as data_file:    
    				item = json.load(data_file)
			item.update({sys.argv[2] : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
			with io.open(sys.argv[3] + '.json', 'w', encoding='utf8') as outfile:
    				str_ = json.dumps(item, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    				outfile.write(to_unicode(str_))
		else:
			print("Can't add {0} to {1}\nThe file {1} doesn't exists!!!".format(sys.argv[2], sys.argv[3]))
	
	elif( sys.argv[1] == 'list' ):
		if os.path.exists(sys.argv[2] + '.json'):
    			with open(sys.argv[2] + '.json') as json_data:
    				d = json.load(json_data)
    				#print(d.keys())
		else:
			print("There is no such user!!!")
	
	#elif( sys.argv[1] == 'delete' ):
		#print("delete")
	else:
		print("Read the manual properly")
except IndexError:
	print( open('readme.txt', 'r').read() )
