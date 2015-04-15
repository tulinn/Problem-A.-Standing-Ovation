def standingOvation(Smax, S, case_num):
	prev = 0
	needed = 0
	# print S
	i = 0
	while i <= Smax:
		if prev < i:
			needed += (i - prev)
			prev += (i - prev)
		prev += S[i]
		i += 1
	return "Case #{}: {}".format(case_num, needed)

if __name__ == '__main__':
	case_num = 1
	#inp = raw_input("Enter: ").split("\n")
	f = open('input.in', 'r')
	for i, line in enumerate(f.read().split("\n")):
		if not line: continue
		if i == 0: # T
			continue
		else:
			inp = line.split(" ")
			Smax = int(inp[0])
			S = [int(x) for x in list(inp[1])] # array of shyness pts
			print standingOvation(Smax, S, case_num)
			case_num += 1
	f.close()