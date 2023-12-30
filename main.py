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
    file_txt = File("file.txt", docs, "This is the content of file.txt.")
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


