import requests
import hashlib
import sys



def hashup_my_password(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

	return sha1password

def pawn_check_api_data(hash_password):
	url = 'https://api.pwnedpasswords.com/range/'+ hash_password
	response = requests.get(url)
	if response.status_code != 200:
		raise RuntimeError(f'Error fething {response.status_code}')
	
	return response

def password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for hash,count in hashes:
		if hash == hash_to_check:
			return count
def password_pawn_check(password):
	sha1password = hashup_my_password(password)
	head,tail = sha1password[:5], sha1password[5:]
	response = pawn_check_api_data(head)
	count = password_leaks_count(response,tail)

	return count
	 

def main(args):
	# for password in args:
	# 	count = password_pawn_check(password)
	# 	if count :
	# 		print(f'Password provided {password} has been used {count} number of times. Please change the password!')
	# 	else:
	# 		print(f'Password provided {password} was not found. Should be good to be used')

	test_password_file = open(args,'r')
	passwords_list = test_password_file.readlines()
	for password in passwords_list:
		count = password_pawn_check(password)
		if count :
			print(f'Password provided {password} has been used {count} number of times. Please change the password!')
		else:
			print(f'Password provided {password} was not found. Should be good to be used')


main(sys.argv[1])








