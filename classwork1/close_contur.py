# հաշվել փակ կոնտուրի մակերեսը: * համարել 1 միավոր, կոնտուրի կողերը(/,\) 0,5 միավոր:

def count_surface(matrix):
    # Լուծում: պետք է տող առ տող անցնենք յուրաքանչյուր սիմվոլի վրայով, ամեն տողի համար հաշվում ենք կողերի քանակը,
    # քանի որ փակ կոնտուր է ապա այն տողերում որտեղ կա կոնտուրի մաս պետք է լինի 2 կող, այսպիսով հաշվում ենք կողերը
    # եւ օգտագործում որպեսզի հասկանանք կոնտուրի մեջ ենք, թե` ոչ: Կոնտուրի մեջ ենք երբ կողերի քանակը 1 է:
    surface=0
    # for line in matrix:
    #     edge_count_in_line=0
    #     for symbol in line:
    #         if symbol=='/' or symbol =='\\':
    #             edge_count_in_line+=1
    #             surface+=0.5
    #         if edge_count_in_line%2==1 and symbol=='*':
    #             surface+=1
    for line in matrix:
        inside=False
        for symbol in line:
            if symbol in ('/','\\'):
                inside = not inside
                surface+=0.5
            if inside and symbol=='*':
                surface+=1

    return surface

if __name__ == "__main__":
    contur = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '/', '\\', '*', '*', '*', '*'],
        ['*', '*', '*', '/', '*', '*', '\\', '*', '*', '*'],
        ['*', '*', '/', '*', '*', '*', '*', '\\', '*', '*'],
        ['*', '*', '\\', '*', '*', '*', '*', '/', '*', '*'],
        ['*', '*', '*', '\\', '*', '*', '/', '*', '*', '*'],
        ['*', '*', '*', '*', '\\', '/', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    for line in contur:
        print(" ".join(line))
    surface=count_surface(contur)
    print(f"Contur's surface is equal to {surface}")