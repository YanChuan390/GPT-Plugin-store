import analysis_method

item = analysis_method.Json()
print("-----------step 1:try different url in the same domain ------------")
item.write_down()
item.inital_excel()
item.save_changes()
print('------------step 2:detect manifest file----------------------')
#
item.handle_list_2(0,'url1')
item.save_changes()
item.handle_list_2(0,'url2')
item.save_changes()
item.handle_list_2(0,'url3')
item.save_changes()
item.handle_list_2(0,'url4')
item.save_changes()
item.handle_list_2(0,'url5')
item.save_changes()

print('---------------------step 3:check api information and request------------------------------')
item.get_api(0)
item.save_changes()

item.get_api_info(0)
item.save_changes()

item.clear_path(0)
item.save_changes()

item.request_result(0)
item.save_changes()
print('---------------------step 4:check request with token------------------------------')
item.check_auth(0)
item.save_changes()

item.detect_token(0)
item.save_changes()

item.request_result(0)
item.save_changes()

print("---------------------step 5:check name and legal----------------------------")
item.check_name(0)
item.save_changes()

item.check_legal(0)