fayl_yollari = ['/home/user/documents/file1.txt', '/home/user/pictures/file2.jpg', '/home/user/videos/file3.mp4']
papka_yollari = [fayl_yoli[:fayl_yoli.rfind('/')] for fayl_yoli in fayl_yollari]
print(papka_yollari)
