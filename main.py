from googledrive import drive
from datetime import date

from settings import Settings

# Auto-iterate through all files in the root folder.
def list_content(folder_id: str) -> None:
    file_list = drive.ListFile(
        {"q": f"'{folder_id}' in parents and trashed=false"}
    ).GetList()
    for file1 in file_list:
        print("title: %s, id: %s" % (file1["title"], file1["id"]))
        # print("filesize: ", file1["fileSize"]) # only works for file type


def get_year_folder_id(system_folder_id: str) -> str:
    pass


def get_month_folder_id(system_folder_id: str) -> str:
    pass


def get_file_size(system, date: date):
    pass


for system in Settings.locations:
    print("System ", system.name)
    list_content(system.folder_id)
    break
