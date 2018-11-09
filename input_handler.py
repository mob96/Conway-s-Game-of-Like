import libtcodpy as libtcod

## PURPOSE: Handle keyboard input ##

def handle_keys(key):
	
	## UTILITY ##
	
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		return {'fullscreen': True}
		
	elif key.vk == libtcod.KEY_ESCAPE:
		return {'exit': True}
		
	return {}