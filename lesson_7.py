# nums = [1, 7, 3, 6, 5, 6]
# # nums = [2, 1, -1]
# pivot = -1
# for i in range(len(nums)):
#     if sum(nums[:i]) == sum(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

# nums = [1, 7, 3, 6, 5, 6]
# # nums = [2, 1, -1]
# pivot = -1
# for i in range(len(nums)):
#     if len(nums[:i]) == len(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

# import re
# text = 'milk how dogs. python'
# match = re.search(r'\w{4}', text) #поиск первого вхождения
# print(match.group())

# matches = re.findall(r'\b\w{4}\b', text) # поиск всех вхождений
# print(matches)

# import re
# text = '1234 123 748 78 5 143'
# matches = re.findall(r'\b\d{3}\b', text)
# print(matches)
# import re

# dates = '10.12.2001 15/01/2004 14.02.14 18-05-2024'
# maches = re.findall(r'\d\d\.\d\d\.\d{4}', dates)
# maches_sub = re.sub(r'\d\d\.\d\d\.\d{4}',r'dd.mm.yyyy', dates) # Замена найденого
# print(maches_sub)

# text = 'Ivan, Bob; Maria: Petr'
# names = re.split(r'[,;:]', ''.join(text.split()))
# print(names)
# import re
# text = '+7999999998 +7 (999)999998 +7 (999)-999-9998 +7 (999)-99-999-78'
# correct_num = re.findall(r'\+7 \(\d{3}\)-\d{2}-\d{3}-\d{2}', text)
# print(correct_num)

# emails = 'testmail.ru test@mail.ru test123@mail.com test@mail!com'
# correct_emails = re.findall(r'\w+@\w{2,20}\.[comru]{2,3}', emails)
# print(correct_emails)
# import re

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi iaculis eget sem in faucibus. In vitae venenatis enim, in facilisis enim. Aliquam condimentum metus at luctus tempus. Quisque ultricies cursus gravida. Proin porta mauris quis dictum tempor. Praesent elementum ipsum ac ipsum feugiat, fringilla vehicula augue tincidunt. Nulla rutrum sit amet nisl id interdum. Pellentesque venenatis eleifend nunc a iaculis. In eget ante erat. Proin ultricies turpis sed sapien commodo, nec eleifend ipsum scelerisque. Nunc non dui lobortis, pharetra mauris at, facilisis ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean imperdiet id augue sit amet aliquet. Quisque at arcu vitae enim auctor volutpat nec eu turpis. In auctor, eros eget faucibus condimentum, elit lectus pulvinar augue, id maximus odio enim sit amet felis.'
# words = re.findall(r'\b\w{4}\b', text)
# print(words)

# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi iaculis eget sem in faucibus. In vitae venenatis enim, in facilisis enim. Aliquam condimentum metus at luctus tempus. Quisque ultricies cursus gravida. Proin porta mauris quis dictum tempor. Praesent elementum ipsum ac ipsum feugiat, fringilla vehicula augue tincidunt. Nulla rutrum sit amet nisl id interdum. Pellentesque venenatis eleifend nunc a iaculis. In eget ante erat. Proin ultricies turpis sed sapien commodo, nec eleifend ipsum scelerisque. Nunc non dui lobortis, pharetra mauris at, facilisis ipsum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean imperdiet id augue sit amet aliquet. Quisque at arcu vitae enim auctor volutpat nec eu turpis. In auctor, eros eget faucibus condimentum, elit lectus pulvinar augue, id maximus odio enim sit amet felis.'
# words = re.findall(r'\w+\,', text)
# print(words)

# reg_znak = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
# chastniki = re.findall(r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', reg_znak)
# taxi = re.findall(r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', reg_znak)
# print(chastniki, taxi)
# import re
#
# import requests
#
# url = 'http://www.columbia.edu/~fdc/sample.html'
# response = requests.get(url)
# text = response.text
# # print(text)
# heading = re.findall(r'<h3 id="\w*">(.*)</h3>', text)
#
# print(heading)
import re

text = '4567'
if re.match(r'\d{4}', text):
    print('ok')


