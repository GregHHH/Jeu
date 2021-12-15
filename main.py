from generate import *

# frame = np.array([
# 		[0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 1, 0],
# 		[0, 0, 1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0, 0],
# 		[0, 0, 1, 0, 0, 1, 0],
# 		[0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 1, 0],
# 		[0, 0, 1, 1, 0, 0, 0],
#         [0, 1, 1, 1, 1, 0, 0],
# 		[0, 0, 0, 0, 0, 1, 0],
# 		[0, 0, 0, 0, 0, 0, 0]])

def print_frame(frame, i):
	print(f"{frame}")
	print(i)

def compute_number_neighbors(paded_frame, index_line, index_column):
	number_neighbors = 0
	for i in range(index_line - 1, index_line + 2):
		for j in range(index_column - 1, index_column + 2):
				number_neighbors += paded_frame[i][j]
	number_neighbors -= paded_frame[index_line][index_column]
	return number_neighbors

def add_padding (frame):
	paded_frame = np.pad(frame, 1, mode='constant')
	return paded_frame

def copy_with_rules(frame):
	size_lin = len(frame)
	size_col = len(frame[0])
	cp_frame = np.zeros((size_lin, size_col), int)
 	
	# TODO: toute la grille n'est pas visitée à cause du -1 (bordures)
	for i in range(1, size_lin - 1):
		for j in range(1, size_col - 1):
			# On applique les règles du Jeu de la Vie
			number_neighbors = compute_number_neighbors(frame, i, j)
			if frame[i][j] == 0 and number_neighbors == 3:
				cp_frame[i][j] = 1
			elif frame[i][j] == 1 and (number_neighbors == 2 or number_neighbors == 3):
				cp_frame[i][j] = 1
			else:
				continue
	return cp_frame

# TODO: Verif avec les cellules qui prennent vie dans la bordure : disparition de la figure :( (encore  incrémenter la taille de la bordure à ce moment ?)
size_lin = int(sys.argv[2]) if len(sys.argv) >= 2 else int(6)
size_col = int(sys.argv[2]) if len(sys.argv) >= 3 else int(6)
density = int(sys.argv[2]) if len(sys.argv) >= 4 else int(15)

i = 0
frame = generate(size_lin, size_col, density)
frame = add_padding(frame)
while True:
	os.system('clear')
	print_frame(frame, i)
	i += 1
	frame = copy_with_rules(frame)
	time.sleep(0.2)
	is_all_zero = np.all((frame == 0))
	if is_all_zero:
		#TODO: finir si la copie du tableau est identique au tableau précédent.
		print_frame(frame, i)
		break
	else:
		continue
	
