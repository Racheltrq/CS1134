import ArrayStack


def get_tag(expr):
	expr = expr.strip()
	n = len(expr)
	i = 0
	left_index = 0
	right_index = 0
	found = False
	while i < n:
		if expr[i] != '<':
			i += 1
		else:
			left_index = i
			while expr[i] != '>':
				i += 1
			right_index = i
			found = True
			break
	if found == False:
		return -1
	tag = expr[left_index : right_index + 1]
	
	if tag.find(' ') != -1:
		index = tag.index(' ')
		if tag[-2] == '/':
			tag = tag[:index] + tag[-2:]
		else:
			tag = tag[:index] + tag[-1]

	return tag



def is_matched(expr):
	s_left = ArrayStack.ArrayStack()
	
	while get_tag(expr) != -1:
		tag = get_tag(expr)
		if '/' not in tag:
			if tag != '<!DOCTYPE>':
				s_left.push(tag)
		else:
			if tag.index('/') == 1:
				temp = s_left.top()
				if tag[2:] == temp[1:]:
					s_left.pop()
				else:
					return False
		index = expr.find('>')
		expr = expr[index+1:]
	return s_left.is_empty()


		

expr = '''<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Style-Type" content="text/css" /> 
    <title>html_file.html</title>
    <link href="/library/skin/tool_base.css" type="text/css" rel="stylesheet" media="all" />
    <link href="/library/skin/morpheus-nyu/tool.css" type="text/css" rel="stylesheet" media="all" />
    <script type="text/javascript" src="/library/js/headscripts.js"></script>
<script type="text/javascript" src="/media-gallery-tool/js/kaltura-upgrade.js"></script>    <style>body { padding: 5px !important; }</style>
  </head>
  <body>
<body> 
<center> 
<h1> The Little Boat </h1> 
</center> 
<p> The storm tossed the little 
boat like a cheap sneaker in an 
old washing machine. The three 
drunken fishermen were used to 
such treatment, of course, but 
not the tree salesman, who even as 
a stowaway now felt that he 
had overpaid for the voyage. </p> 
<ol> 
<li> Will the salesman die? </li> 
<li> What color is the boat? </li> 
<li> And what about Naomi? </li> 
</ol> 
</body> 
  </body>
</html>
'''
print(is_matched(expr))