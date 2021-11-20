def CodelandUsernameValidation(strParam):
  str_list = strParam
  result = True
  if str_list[-1] == "_": result = False
  elif not str_list[0].isalpha(): result = False
  elif (len(strParam) <4 or len(strParam) >= 25): result = False
  elif not strParam.isalnum() and "_" not in strParam: result = False    
  return result 
  
  
# keep this function call here 
print(CodelandUsernameValidation("aa_")) #false
print(CodelandUsernameValidation("1")) #false
print(CodelandUsernameValidation("u__hello_world123")) #true
print(CodelandUsernameValidation("u__hello_world123")) #true