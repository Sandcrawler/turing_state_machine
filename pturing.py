import sys

def logger(log_print):
	print(f"{log_print}")

def turing_state_machine_01(instruction_set):
	input_instructions = {}
	if int(instruction_set) == c:
		#based on busy beaver game input instructions
		#https://en.wikipedia.org/wiki/Busy_beaver
		#00A = 0 written, 0 move left, go to A
		#11E = 1 written, 1 move right, go to E
		input_instructions.update({"A0": ""})
		input_instructions.update({"A1": ""})
		input_instructions.update({"B0": ""})
		input_instructions.update({"B1": ""})
		input_instructions.update({"C0": ""})
		input_instructions.update({"C1": ""})
		input_instructions.update({"D0": ""})
		input_instructions.update({"D1": ""})
		input_instructions.update({"E0": ""})
		input_instructions.update({"E1": ""})
	elif int(instruction_set) == 5:
		#5 state - 2 symbol
		input_instructions.update({"A0": "11B"})
		input_instructions.update({"A1": "10C"})
		input_instructions.update({"B0": "11C"})
		input_instructions.update({"B1": "11B"})
		input_instructions.update({"C0": "11D"})
		input_instructions.update({"C1": "00E"})
		input_instructions.update({"D0": "10A"})
		input_instructions.update({"D1": "10D"})
		input_instructions.update({"E0": "11H"})
		input_instructions.update({"E1": "00A"})
	elif int(instruction_set) == 4:
		#4 state - 2 symbol
		input_instructions.update({"A0": "11B"})
		input_instructions.update({"A1": "10B"})
		input_instructions.update({"B0": "10A"})
		input_instructions.update({"B1": "00C"})
		input_instructions.update({"C0": "11H"})
		input_instructions.update({"C1": "10D"})
		input_instructions.update({"D0": "11D"})
		input_instructions.update({"D1": "01A"})
	elif int(instruction_set) == 3:
		#3 state = 2 symbol
		input_instructions.update({"A0": "11B"})
		input_instructions.update({"A1": "11H"})
		input_instructions.update({"B0": "01C"})
		input_instructions.update({"B1": "11B"})
		input_instructions.update({"C0": "10C"})
		input_instructions.update({"C1": "10A"})
	elif int(instruction_set) == 2:
		#2 state - 2 symbol
		input_instructions.update({"A0": "11B"})
		input_instructions.update({"A1": "10B"})
		input_instructions.update({"B0": "10A"})
		input_instructions.update({"B1": "11H"})
	else:
		#1 state - 2 symbol
		input_instructions.update({"A0": "11H"})
		input_instructions.update({"A1": "11A"})
	logger(f"{input_instructions}")
	loop_count = 0
	position = 0
	dict = { 0: 0 }
	instruction = "00A"
	while "H" != instruction[2:]:
		card =  str(instruction[2:]) + str((dict.get(int(position), 0)))
		instruction = input_instructions[card]
		dict[position] = int(instruction[0:1])
		position = int(position) + int(instruction[1:2])
		if int(instruction[1:2]) == 0:
			if int(position) == 0:
				new_dict = {}
				for k, v in dict.items():
					new_dict[int(k)+1] = int(v)
				dict = { 0: 0 }
				dict.update(new_dict)
			else:
				position -= 1
		loop_count += 1
		#move the below in/out of loop for when to print output
		arr = str(list(dict.values()))
		arr = arr.replace(",", "").replace("\'", "").replace(" ", "")
		logger(f"{arr}")

def main(to_run):
	import time
	start_time = time.time()
	logger(f"## start:{start_time}")
	turing_state_machine_01(to_run)
	end_time = time.time()
	logger(f"##   end:{end_time}")
	total_time = end_time - start_time
	logger(f"## total:{total_time}")

main(sys.argv[1])
exit(0)
