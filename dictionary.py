# dictionary 예제
person = {'name': '홍길동', 'age': 25, 'address': '서울시 용산구 이촌동'}
name = person['name']

# print(name)

print(f"이름은 {person['name']}이고, 나이는 {person['age']}세, 주소는 {person['address']}입니다.")

city = person.get("address", "서울시")
person['country'] = '대한민국'

print(person)
country = person.get('country', '한국')
print(f"국적은 {country}입니다.")
