import libtcodpy as libtcod
from input_handler import handle_keys
from entity import Entity
from renderer import render_all, clear_all
from gamemap import GameMap

def main():
	## SETUP ##
	screen_width = 80
	screen_height = 65
	fps_limit = 10
	
	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
	libtcod.console_init_root(screen_width, screen_height, 'The Game of Life', False)
	libtcod.sys_set_fps(fps_limit)
	
	con = libtcod.console_new(screen_width, screen_height)
	key = libtcod.Key()
	mouse = libtcod.Mouse()
	map = GameMap(screen_width, screen_height)
	
	## GAME LOOP ##
	while not libtcod.console_is_window_closed():
	
		## ENTITY UPDATES AND RENDERING ##
		entities = map.get_entities()
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
		render_all(con, entities, screen_width, screen_height)
		libtcod.console_flush()
		clear_all(con, entities)
		map.update_tiles()
		
		
		## CALLS TO INPUT HANDLING ##
		input = handle_keys(key)
		exit = input.get('exit')
		fullscreen = input.get('fullscreen')
		
		if exit:
			return True
			
		if fullscreen:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
			

if __name__ == '__main__':
	main();