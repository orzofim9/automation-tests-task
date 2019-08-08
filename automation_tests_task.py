import os, json, random, sys, datetime
from os import path	

def run_test(scenario_data):
	"""
		Tests scenario_data(username and passward) and return the result.
	"""
# Random choice between "successful login" and "login failed", which should simulate an a "run_test" test.
	test_result = random.choice(["successful login", "login failed"])
	return test_result	

		
def save_data_to_file(file_data, file_path):
	"""
		Gets a data from file and write it to a txt file in a given path.
	"""
# Open file and write in it the updated file_name(with actual_result).
	with open(file_path, 'a') as fp:
		fp.write('{}\n'.format(json.dumps(file_data))) 


def print_path(file_name, file_path):
	"""
		Print the path of a file.
	"""
# Get the current directory path and add to it the file name for full path.
	file_path = (os.path.join(os.getcwd(), file_path)) 
	print(file_name, file_path)
	
	
def compare_results(test_scenario, test_result):
	"""
		Compare between expected result and actual result and return the scenario's username in a case of mismatch.
	"""
	expected_result = test_scenario.get("expected_result")  
	compare_results = (expected_result == test_result)
	
# If the test failed, get it's username's test and add it to set_failed_usernames.
	if not compare_results:
		return scenario_data.get("username")
	

"""
	Given an input file path, the script runs tests scenarios and compares the actual results with the expected results.
	the output of the script is two files, one is a file containing a list of usernames in which the actual results and the expected results were mismatched.
	and the other is the output of the tests scenarios.
"""
try:
	file = sys.argv[1]
except IndexError:
	raise Exception('An exception occurred, you need to  write your input file path. See the \"README\" File for an example.')
	
set_failed_usernames = set()
current_time = datetime.datetime.now()
failed_usernames_path = 'failed_usernames {}.txt'.format(current_time.strftime("%Y-%m-%d %H-%M.txt"))
test_result_path = 'test_result {}.txt'.format(current_time.strftime("%Y-%m-%d %H-%M"))
#failed_usernames_path = 'failed_usernames {}-{}.txt'.format(current_time.strftime("%Y-%m-%d %H-%M"), current_time.second ) 
#test_result_path = 'test_result {}-{}.txt'.format(current_time.strftime("%Y-%m-%d %H-%M"), current_time.second )

# Open file.
fp = open(file, 'r')	
for line in fp:
# Extract scenario_data(username and passward) from test_scenario.
	try:
		test_scenario = json.loads(line)
	except json.decoder.JSONDecodeError:
		print("An exception occurred, invalid line in \"input.txt\". See the \"README\" File for an example.")
		print("The inavlid line is: ", line)
		continue
	scenario_data = test_scenario.get("scenario_data") 
	
# Call run_test function and add it's value to actual result in test_scenario.
	test_result = run_test(scenario_data) 
	test_scenario.update({'actual_result' : test_result}) 
	username = compare_results(test_scenario, test_result) 
	if username != None:
		set_failed_usernames.add(username)	
# Call save_data_to_file function.
	save_data_to_file(test_scenario, test_result_path)
	
failed_usernames = list(set_failed_usernames)
save_data_to_file(failed_usernames, failed_usernames_path)

# Close file and call print_pathes function.
fp.close() 
print_path("Test result file path: ", test_result_path)
print_path("Username failed file path: ", failed_usernames_path)