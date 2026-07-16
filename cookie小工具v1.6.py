from DrissionPage import ChromiumPage, ChromiumOptions
import time
import os

# 文件名
txt_filename = 'cookie.txt'

# 删除旧文件
if os.path.exists(txt_filename):
	os.remove(txt_filename)

# 运行程序
print('=' * 75)
print('程序名称: cookie小工具v1.6')
print('原创作者: 马哥python说')
print('最新版本: 公众号"老男孩的平凡之路"后台回复: ck')
print('=' * 75)
print('注意事项：')
print('1、提前安装好Chrome浏览器(如有请忽略)')
print('2、小红书: 如需获取多cookie，必须一个账号对应一次登录，而不是同账号登录多次！！')
print('=' * 75)
print('\n1.抖音\n2.快手\n3.小红书\n4.小红书蒲公英\n5.知乎\n6.哔哩哔哩\n7.百度\n8.微博pc端\n9.微博m端')
choice = input('\n想获取哪个平台的cookie? 请输入对应的数字: ')
try:
	attempt = 0
	while True:
		attempt += 1
		# 打开登录页面
		if choice == '1':
			plat_name = '抖音'
			plat_url = 'https://www.douyin.com'
		elif choice == '2':
			plat_name = '快手'
			plat_url = 'https://www.kuaishou.com'
		elif choice == '3':
			plat_name = '小红书'
			plat_url = 'https://www.xiaohongshu.com'
		elif choice == '4':
			plat_name = '小红书蒲公英'
			plat_url = 'https://pgy.xiaohongshu.com'
		elif choice == '5':
			plat_name = '知乎'
			plat_url = 'https://www.zhihu.com'
		elif choice == '6':
			plat_name = '哔哩哔哩'
			plat_url = 'https://www.bilibili.com'
		elif choice == '7':
			plat_name = '百度'
			plat_url = 'https://www.baidu.com'
		elif choice == '8':
			plat_name = '微博pc端'
			plat_url = 'https://www.weibo.com'
		elif choice == '9':
			plat_name = '微博m端'
			plat_url = 'https://m.weibo.cn'
		else:
			print('非法选项，3s后退出程序！')
			time.sleep(3)
			break
		# 初始化浏览器选项
		co = ChromiumOptions()
		co.incognito()  # 匿名模式
		# 初始化浏览器对象
		page = ChromiumPage(co)
		page.get(plat_url)
		# 等待用户扫码登录
		a = input(f"\n[{plat_name}][第{attempt}次]请登录！先完成登录，再按Enter键，顺序不要反了！！（退出按Q）")
		if a in ['q', 'Q']:
			print(f'\n请检查当前文件夹的: {txt_filename}')
			print('5s后程序退出!')
			time.sleep(5)
			# 关闭浏览器
			page.quit()
			break
		# 获取cookie
		ck_str = ''
		for cookie in page.cookies():
			ck_item = cookie['name'] + '=' + cookie['value']
			ck_str += ck_item + ';'
		cookie_value = ck_str
		# 特殊处理: 小红书
		if choice == '3':
			# 分割字符串  
			parts = cookie_value.split(";")
			# 找到abRequestId并排到前面
			abRequestId_value = ""
			for part in parts:
			    if part.startswith("abRequestId="):
			        abRequestId_value = part
			        parts.remove(part)
			        break
			# 重新组合字符串
			cookie_value = f"{abRequestId_value}; " + "; ".join(parts)
		# 保存当前的 cookie 到TXT文件
		with open(txt_filename, mode='a+', encoding='utf-8') as file:
			file.write(f'{cookie_value}\n\n')  # 写入txt，末尾加空行
		print(f"\n第{attempt}次的cookie已保存: {cookie_value}")
		# 关闭浏览器
		page.quit()
		# 小红书支持多次获取cookie，其他平台获取一次后退出
		if choice == '3':
			cont = input('\n是否继续获取下一个cookie？（注意：是换一个登录账号，而非同账号！）请选择(y/n): ')
			if cont.lower() != 'y':
				# 提醒用户检查结果
				print(f'\n请检查当前文件夹的: {txt_filename}')
				print('5s后程序退出!')
				time.sleep(5)
				break
		else:
			print(f'\n请检查当前文件夹的: {txt_filename}')
			print('5s后程序退出!')
			time.sleep(5)
			break

except KeyboardInterrupt:
	print("\n用户已取消登录，退出程序！")
except Exception as e:
	print(f"\n发生错误: {e}")

# 清理txt文件末尾多余的空行
if os.path.exists(txt_filename):
	with open(txt_filename, 'r', encoding='utf-8') as f:
		content = f.read().rstrip('\n')
	with open(txt_filename, 'w', encoding='utf-8') as f:
		f.write(content)
