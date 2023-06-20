def create_hashtags(caption:str):
    allowed_characters = "abcdefghijklmnopqrstuvwxyz1234567890_"

    words: List = caption.split(' ')
    hashtags = []

    for word in words:

        if word.startswith('#'):
            hashtag: str = ''
            spoilt:bool = False
            for i in range(len(word)):
                letter = word[i]
                
                if (letter in allowed_characters or letter.lower() in allowed_characters) and len(hashtag) < 15:
                    if spoilt == False:
                        hashtag += letter.lower()
                else:
                    if letter != '#':
                        spoilt = True
                    elif letter == '#' and hashtag!='':
                        hashtags.append(hashtag)
                        hashtag = ''

            hashtags.append(hashtag)

    print(hashtags)



create_hashtags('This is my #fiFtH post on #rael_arts#ads#dsa #myveryownhashtagonpulsar')
