import sys
import os
import json
import datetime
import io
from bottle import run, route

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
			item.update({sys.argv[2] : {'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}})
			with io.open(sys.argv[3] + '.json', 'w', encoding='utf8') as outfile:
    				str_ = json.dumps(item, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    				outfile.write(to_unicode(str_))
		else:
			print("Can't add {0} to {1}\nThe file {1} doesn't exists!!!".format(sys.argv[2], sys.argv[3]))
	
	elif( sys.argv[1] == 'list' ):
		if os.path.exists(sys.argv[2] + '.json'):
			with open(sys.argv[2] + '.json') as data_file:
				d = json.load(data_file)
			print(*d.keys())
		else:
			print("There is no such user!!!")
	
	#elif( sys.argv[1] == 'delete' ):
		#print("delete")
	elif( sys.argv[1] == 'show' ):
		@route('/show/<name>')
		def show(name):
			if os.path.exists(sys.argv[2] + '.json'):
				name = sys.argv[2]
				with open(sys.argv[2] + '.json') as data_file:
					d = json.load(data_file)
				ites = ['<li>{}</li>'.format(i) for i in d.keys()]
				return ''.join(ites)
		run(reload = True, debug = True)

	else:
		print("Read the manual properly")
except IndexError:
	print( open('readme.txt', 'r').read() )
