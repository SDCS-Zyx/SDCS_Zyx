# -*- coding:UTF-8 -*- 

import copy

def get_charge_pos(board) :
	way = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
	ret = []
	
	for i in range(15) :
		for j in range(15) :
			if board[i][j] != 0 :
				for w in way :
					pos = (i + w[0], j + w[1])
					if pos[0] not in range(15) or pos[1] not in range(15) :
						continue
					if (board[pos[0]][pos[1]] == 0) and (pos not in ret) :
						ret.append(pos)
						
	return ret
	
def get_line_score(line) :
	#连五 ： 100000, 活四，双冲四，冲四活三 ： 10000, 双活三 ： 5000, 活三眠三 ： 1000
	#眠四 ： 500, 活三 ： 200, 双活二 ： 100, 眠三 ： 50, 活二眠二 ： 10, 活二 ： 5
	#眠二 ：3, 死四 ： -5, 死三 ： -5, 死二 ： -5
	
	score = 0
	
	#连五
	for i in line :
		if i.find('22222') != -1 :
			score += 100000
			break
	
	#活四
	for i in line :
		if i.find('022220') != -1 :
			score += 50000
			break
	
	#双冲四
	count = 0
	for i in line :
		for size in ['022221', '122220', '20222', '22202', '22022'] :
			if i.find(size) != -1 :
				count += 1
				break
				
		if count == 2 :
			score += 10000
			break
	
	#冲四活三
	ft = [0,0]
	for i in line :
		if not ft[0] :
			for size in ['022221', '122220', '20222', '22202', '22022'] :
				if i.find(size) != -1 :
					ft[0] = 1
					break
		
		if not ft[1] :
			for size in ['02220', '2022', '2202'] :
				if i.find(size) != -1 :
					ft[1] = 1
					break
		
		if ft[0] and ft[1] :
			score += 10000
			break
	
	#双活三
	count = 0
	for i in line :
		for size in ['02220', '2022', '2202'] :
			if i.find(size) != -1 :
				count += 1
				break
				
		if count == 2 :
			score += 10000
			break
			
	#活三眠三
	tt = [0,0]
	for i in line :
		if not tt[0] :
			for size in ['02220', '2022', '2202'] :
				if i.find(size) != -1 :
					tt[0] = 1
					break
				
		if not tt[1] :
			for size in ['002221', '122200', '020221', '122020', '022021', '120220', '20022', '22002', '20202', '1022201'] :
				if i.find(size) != -1 :
					tt[1] = 1
				break
		
		if tt[0] and tt[1] :
			score += 1000
			break
	
	#眠四
	
	#活三
	count = 0
	for i in line :
		for size in ['02220', '2022', '2202'] :
			if i.find(size) != -1 :
				count += 1
				break
	score += count * 200
	
	#双活二
	count = 0
	for i in line :
		for size in ['002200', '02020', '2002'] :
			if i.find(size) != -1 :
				count += 1
				break
		if count == 2 :
			score += 100
			break
	
	#眠三
	count = 0
	for i in line :
		for size in ['002221', '122200', '020221', '122020', '022021', '120220', '20022', '22002', '20202', '1022201'] :
			if i.find(size) != -1 :
				count += 1
				break
	score += count * 50
	
	#活二眠二
	dd = [0,0]
	for i in line :
		if not dd[0] :
			for size in ['002200', '02020', '2002'] :
				if i.find(size) != -1 :
					dd[0] = 1
					break			
		
		if not dd[1] :
			for size in ['000221', '122000', '002021', '120200', '020021', '120020', '20002'] :
				if i.find(size) != -1 :
					dd[1] = 1
					break
					
		if dd[0] and dd[1] :
			score += 10
			break
	
	#活二
	count = 0
	for i in line :
		for size in ['002200', '02020', '2002'] :
			if i.find(size) != -1 :
				count += 1
				break
	score += count * 5
	
	#眠二
	count = 0
	for i in line :
		for size in ['000221', '122000', '002021', '120200', '020021', '120020', '20002'] :
			if i.find(size) != -1 :
				count += 1
				break
	score += count * 3
	
	#死四，死三，死二
	count = 0
	for i in line :
		if i.find('122221') != -1 :
			count += 1
		if i.find('12221') != -1 :
			count += 1
		if i.find('1221') != -1 :
			count += 1
	score += count * -5
	
	return score
		
	
def get_score(pos, board) :
	
	ori = copy.deepcopy(board)
	ori[pos[0]][pos[1]] = 2
	
	#横，竖
	h = str(ori[pos[0]])[1:-1].replace(',', '').replace(' ', '')
	s = str([ori[i][pos[1]] for i in range(15)])[1:-1].replace(',', '').replace(' ', '')
	
	#左斜
	lx = str([ori[i][i - pos[0] + pos[1]] for i in range(15) if (i - pos[0] + pos[1]) in range(15)])[1:-1].replace(',', '').replace(' ', '')
	
	#右斜
	rx = str([ori[i][pos[0] + pos[1] - i] for i in range(15) if (pos[0] + pos[1] - i) in range(15)])[1:-1].replace(',', '').replace(' ', '')
	
	return get_line_score([h, s, lx, rx])				
	
def opp_board(board) :
	o_board = [[0] * 15 for i in range(15)]	
	
	for i in range(15) :
		for j in range(15) :
			if board[i][j] != 0 :
				o_board[i][j] = 1 if board[i][j] == 2 else 2
				
	return o_board

def get_pos(board) :
	pos = get_charge_pos(board)
	
	get = (-1, -1)
	score = -float("inf")
	
	for p in pos :
		o_board = opp_board(board)
		s = get_score(p, board) + get_score(p, o_board)
		if s > score :
			get = p
			score = s
			
	return get
