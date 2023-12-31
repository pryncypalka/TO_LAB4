from prompt import Prompt

from tree_structure.Directory import Directory
from tree_structure.File import File

from Path_to_Directory import Path_to_Directory

def create_tree_structure():
    # Tworzenie struktury drzewa plików
    root = Directory("/", None)

    # Katalog "usr"
    usr = Directory("usr", root)
    root.add_child(usr)

    # Katalog "admin" w "usr"
    admin = Directory("admin", usr)
    usr.add_child(admin)

    # Katalog "dev" w "root"
    dev = Directory("dev", root)
    root.add_child(dev)



    # Katalog "docs" w "root"
    docs = Directory("docs", root)
    root.add_child(docs)

    # Plik "file.txt" w "docs"
    file_txt = File("file.txt", docs,
    """Ile dałbym, by zapomnieć Cię
Wszystkie chwile te, które są na nie
Bo chcę (bo chcę)
Nie myśleć o tym już
Zdmuchnąć wszystkie wspomnienia niczym zaległy kurz
Tak już (tak już)
Po prostu nie pamiętać sytuacji, w których serce klęka
Wiem, nie wyrwę się, chociaż bardzo chcę
Mam nadzieję, że to wiesz i Ty
Znowu widzę Ciebie przed swoimi oczami
Znowu zasnąć nie mogę, owładnięty marzeniami
Wszystko poświęcam myśli, że byłaś kiedyś blisko
Kiedy czułem Ciebie obok, wtedy czułem, że mam wszystko
Tyle zostało po mnie, tylko Ty i setki wspomnień
Ile dałbym za to, by móc o tym już zapomnieć
Teraz nie ma Nas i nie chcę być tam gdzie Ty jesteś
Znowu staniesz przede mną, zawsze robisz mi to we śnie
Będę patrzył jak odchodzisz, chociaż chciałbym się odwrócić
Będę myślał ile dałbym komuś kto by czas zawrócił
Kto by zatrzymał wskazówki, tylko na ten jeden moment
W chwili, w której Cię poznałem poszedłbym już w drugą stronę
Ile dałbym, by zapomnieć Cię
Wszystkie chwile te, które są na nie
Bo chcę (bo chcę)
Nie myśleć o tym już
Zdmuchnąć wszystkie wspomnienia niczym zaległy kurz
Tak już (tak już)
Po prostu nie pamiętać sytuacji, w których serce klęka
Wiem, nie wyrwę się, chociaż bardzo chcę
Mam nadzieję, że to wiesz i Ty
To był sen na jawie, gdy marzenia się spełniały
Wszystko takie realne, chwile szybko tak mijały
Tylko my, zamknięci w czterech ścianach, a tak wolni
Ważna Ty byłaś obok, a ja czułem się spokojny
Pamiętasz jeszcze? Te dni, całe miesiące
Pamiętasz? Chcesz zapomnieć? Ja nie mogę, wiem, że błądzę
Snute kiedyś opowiastki, ja, Ty i srebrna taca
Kiedyś to nie przerażało, już do tego nie chcę wracać
Aura zepsucia w powietrzu, tracisz te 50 procent
Chcę zapomnieć o Tobie, zatrzeć w pamięci te noce
By odeszły w niepamięć, chwile, które zwałem złotem
Tamte chwile to tombak, bo już wiem co było potem
Ile dałbym, by zapomnieć Cię
Wszystkie chwile te, które są na nie
Bo chcę (bo chcę)
Nie myśleć o tym już
Zdmuchnąć wszystkie wspomnienia niczym zaległy kurz
Tak już (tak już)
Po prostu nie pamiętać sytuacji, w których serce klęka
Wiem, nie wyrwę się, chociaż bardzo chcę
Mam nadzieję, że to wiesz i Ty
Moje myśli spiętrzone wokół jednej chwili
Kiedyś ta krótka potrafiła czas umilić
Teraz stojąc jakby obok wciąż się przyglądam
Już nie cieszy jak kiedyś, wspominam, myślę dokąd zdążam
Inne cele w życiu, inne plany i pragnienia
Muszę wszystko pozmieniać, tak jak czas wszystko zmienia
To co było nie wróci, wiem, choć czasem mam nadzieję
Po co mam więc pamiętać, ktoś by powiedział „stare dzieje"
Wiem to, nie mogę zapomnieć jak było dobrze
Wiem to, skończyło się, mój własny pogrzeb
Wiem to, i proszę Boga, nigdy więcej
Niech nie pozwoli na to, by ktoś trafił w moje serce
Ile dałbym, by zapomnieć Cię
Wszystkie chwile te, które są na nie
Bo chcę (bo chcę)
Nie myśleć o tym już
Zdmuchnąć wszystkie wspomnienia niczym zaległy kurz
Tak już (tak już)
Po prostu nie pamiętać sytuacji, w których serce klęka
Wiem, nie wyrwę się, chociaż bardzo chcę
Mam nadzieję, że to wiesz i Ty""")
    docs.add_child(file_txt)

    return root



# def display_tree(node, indent=0):
#     print("  " * indent + f"{node.get_name()}/")
#     if isinstance(node, Directory):
#         for child in node.get_children():
#             display_tree(child, indent + 1)
#     elif isinstance(node, File):
#         print("  " * (indent + 1) + f"{node.get_name()} ({len(node.get_content())} bytes)")


def main():
    root = create_tree_structure()
    # display_tree(root)
    prompt = Prompt()
    prompt.update_location(root)
    Path_to_Directory._root_directory = root
    prompt.run()



if __name__ == '__main__':
    main()


