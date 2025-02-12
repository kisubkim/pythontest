#기본 매개변수
def welcome(city, name = 'guest', room=None):
    if room is None:
        room = []

    room.append(101)
    print(f"Welcome, {name}! This is {city}. Room: {room}")
    

welcome("Seoul")
welcome("Seoul", "James")

#키워드 인자
welcome("Seoul", room=[102])
welcome("Seoul", name="Brown", room=[103])
welcome("Seoul", room=[104], name="Smith")
